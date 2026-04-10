from flask import Flask, render_template, request
from scheduler.scheduler import Scheduler

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generar", methods=["POST"])
def generar():
    try:
        # Leer formulario
        usar_fijo = request.form.get("fijo")
        asesor = request.form.get("asesor")

        # Debug (puedes quitar luego)
        print("Checkbox:", usar_fijo)
        print("Asesor:", asesor)

        # Lógica correcta
        if usar_fijo == "on" and asesor:
            scheduler = Scheduler(asesor_fijo_apertura=asesor)
        else:
            scheduler = Scheduler()

        df = scheduler.generar_planeacion()

        if df is None or df.empty:
            print("No se generaron datos")
            return render_template("result.html", tabla=[])

        data = df.to_dict(orient="records")

        return render_template("result.html", tabla=data)

    except Exception as e:
        print(f"Error en la app: {e}")
        return render_template("result.html", tabla=[])


if __name__ == "__main__":
    app.run(debug=True)