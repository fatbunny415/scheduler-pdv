📄 README.md
# Sistema de Planeación de Turnos - PDV

Aplicación web desarrollada en Flask que permite generar automáticamente la asignación de turnos para asesores utilizando optimización con OR-Tools.

---

## 🚀 Características

- Generación automática de turnos (apertura, intermedio, cierre)
- Exclusión de domingos y festivos (Colombia)
- Rotación inteligente de turnos
- Opción de asesor fijo en apertura
- Restricción de no repetición de turnos semanales
- Interfaz web sencilla para generación de planeación

---

## 🧠 Tecnologías utilizadas

- Python
- Flask
- OR-Tools (Google Optimization)
- Pandas
- Holidays

---

## ⚙️ Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/fatbunny415/scheduler-pdv.git
cd scheduler-pdv
Crear entorno virtual:
python -m venv venv
Activar entorno:

Windows

venv\Scripts\activate.ps1

Linux / Mac

source venv/bin/activate
Instalar dependencias:
pip install -r requirements.txt
▶️ Ejecución
python app.py

Abrir en navegador:

http://127.0.0.1:5000
🧩 Lógica del sistema

El sistema utiliza programación con restricciones (CP-SAT) para modelar el problema de asignación de turnos:

Cada asesor trabaja un turno por día
Todos los turnos deben ser cubiertos
No se asignan turnos en domingos ni festivos
Se garantiza rotación de turnos
Se evita repetición del mismo turno en semanas consecutivas
Permite fijar un asesor en apertura
📊 Estructura del proyecto
scheduler-pdv/
│
├── app.py
├── requirements.txt
├── scheduler/
│   └── scheduler.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── result.html

## 👨‍💻 Autor

**Daniel Alejandro Cardona Rico**  
**cardonadeveloper@gmail.com**
Desarrollador de Software (SENA)

- 💼 Enfoque: Backend y optimización de procesos  
- 🧠 Intereses: Desarrollo web, lógica de negocio, OR-Tools  
- 📍 Colombia