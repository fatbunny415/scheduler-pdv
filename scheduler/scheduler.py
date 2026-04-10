from ortools.sat.python import cp_model
import pandas as pd
from datetime import date, timedelta
import holidays


class Scheduler:
    def __init__(self, asesor_fijo_apertura=None):
        self.asesores = ["Asesor 1", "Asesor 2", "Asesor 3"]
        self.turnos = ["apertura", "intermedio", "cierre"]

        self.asesor_fijo_apertura = asesor_fijo_apertura

        self.hoy = date.today()
        self.fin = self.hoy + timedelta(days=30)

        self.festivos = holidays.Colombia(years=[self.hoy.year, self.fin.year])

        self.fechas = self._generar_rango_fechas()

    def _generar_rango_fechas(self):
        fechas = []
        actual = self.hoy

        while actual <= self.fin:
            fechas.append(actual)
            actual += timedelta(days=1)

        return fechas

    def generar_planeacion(self):
        try:
            model = cp_model.CpModel()

            # =========================
            # DÍAS LABORALES
            # =========================
            dias_laborales = [
                i for i, f in enumerate(self.fechas)
                if f.weekday() != 6 and f not in self.festivos
            ]

            # =========================
            # VARIABLES
            # =========================
            x = {}

            for a in self.asesores:
                for t in self.turnos:
                    for d in dias_laborales:
                        x[(a, t, d)] = model.NewBoolVar(f"x_{a}_{t}_{d}")

            # =========================
            # RESTRICCIONES BASE
            # =========================

            # 1. Cada turno cubierto por 1 asesor
            for d in dias_laborales:
                for t in self.turnos:
                    model.Add(sum(x[(a, t, d)] for a in self.asesores) == 1)

            # 2. Cada asesor trabaja 1 turno por día
            for d in dias_laborales:
                for a in self.asesores:
                    model.Add(sum(x[(a, t, d)] for t in self.turnos) == 1)

            # =========================
            # CASO 1: ASESOR FIJO
            # =========================
            if self.asesor_fijo_apertura:

                # Fijar apertura
                for d in dias_laborales:
                    model.Add(x[(self.asesor_fijo_apertura, "apertura", d)] == 1)

                otros = [a for a in self.asesores if a != self.asesor_fijo_apertura]

                semanas = {}
                for i in dias_laborales:
                    semana = self.fechas[i].isocalendar()[1]
                    semanas.setdefault(semana, []).append(i)

                toggle = True

                for _, dias in semanas.items():
                    for d in dias:
                        if toggle:
                            model.Add(x[(otros[0], "intermedio", d)] == 1)
                            model.Add(x[(otros[1], "cierre", d)] == 1)
                        else:
                            model.Add(x[(otros[0], "cierre", d)] == 1)
                            model.Add(x[(otros[1], "intermedio", d)] == 1)

                    toggle = not toggle

            # =========================
            # CASO 2: SIN ASESOR FIJO
            # =========================
            else:
                for i in dias_laborales:
                    fecha_actual = self.fechas[i]
                    semana_actual = fecha_actual.isocalendar()[1]
                    dia_semana = fecha_actual.weekday()

                    for j in dias_laborales:
                        fecha_siguiente = self.fechas[j]

                        if (
                            fecha_siguiente.isocalendar()[1] == semana_actual + 1 and
                            fecha_siguiente.weekday() == dia_semana
                        ):
                            for a in self.asesores:
                                for t in self.turnos:
                                    model.Add(
                                        x[(a, t, i)] + x[(a, t, j)] <= 1
                                    )

            # =========================
            # SOLVER
            # =========================
            solver = cp_model.CpSolver()
            status = solver.Solve(model)

            if status != cp_model.OPTIMAL:
                raise Exception("No se encontró solución")

            return self._crear_dataframe(x, solver, dias_laborales)

        except Exception as e:
            print(f"Error: {e}")
            return None

    def _crear_dataframe(self, x, solver, dias_laborales):
        data = []

        for i, fecha in enumerate(self.fechas):
            fecha_str = fecha.strftime("%d/%m")
            dia_str = self._dia_espanol(fecha)

            es_laboral = i in dias_laborales

            if es_laboral:
                for a in self.asesores:
                    for t in self.turnos:
                        if solver.Value(x[(a, t, i)]) == 1:
                            data.append({
                                "Fecha": fecha_str,
                                "Dia": dia_str,
                                "Asesor": a,
                                "Turno": t
                            })
            else:
                data.append({
                    "Fecha": fecha_str,
                    "Dia": dia_str,
                    "Asesor": "",
                    "Turno": "N/A"
                })

        return pd.DataFrame(data)

    def _dia_espanol(self, fecha):
        dias_map = {
            0: "Lunes",
            1: "Martes",
            2: "Miércoles",
            3: "Jueves",
            4: "Viernes",
            5: "Sábado",
            6: "Domingo"
        }
        return dias_map[fecha.weekday()]