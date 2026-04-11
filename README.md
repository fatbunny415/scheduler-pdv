# Sistema de Planeación de Turnos - PDV

Aplicación web desarrollada en Flask que permite generar automáticamente la asignación de turnos para asesores utilizando optimización con OR-Tools.

---

## ⚙️ Requisitos previos

Antes de instalar el proyecto necesitas tener instalado:

### 🐍 Python (OBLIGATORIO)

Descargar Python 3.10 o superior:

👉 https://www.python.org/downloads/

Durante la instalación en Windows:

✔ Marca la opción:  
`Add Python to PATH`

---

### ✔ Verificar instalación

```bash
python --version

o en algunos sistemas:

python3 --version
📦 Instalación del proyecto
1. Clonar el repositorio
git clone https://github.com/fatbunny415/scheduler-pdv.git
cd scheduler-pdv
2. Crear entorno virtual
Windows:
python -m venv venv
Linux / Mac:
python3 -m venv venv
3. Activar entorno virtual
Windows (PowerShell):
venv\Scripts\activate.ps1
Windows (CMD):
venv\Scripts\activate.bat
Linux / Mac:
source venv/bin/activate
4. Instalar dependencias
pip install -r requirements.txt
▶️ Ejecución del proyecto
python app.py
🌐 Acceder a la aplicación

Abrir en el navegador:

http://127.0.0.1:5000
```
🧠 Lógica del sistema

El sistema utiliza programación con restricciones (CP-SAT) para modelar el problema de asignación de turnos:

Cada asesor trabaja un turno por día
Todos los turnos deben ser cubiertos
No se asignan turnos en domingos ni festivos
Se garantiza rotación de turnos
Se evita repetición del mismo turno en semanas consecutivas
Permite fijar un asesor en apertura
📊 Estructura del proyecto
```bash
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
```
👨‍💻 Autor

Daniel Alejandro Cardona Rico
📧 cardonadeveloper@gmail.com

🎓 Desarrollador de Software (SENA)

💼 Enfoque: Backend y optimización de procesos
🧠 Intereses: Desarrollo web, lógica de negocio, OR-Tools
📍 Colombia