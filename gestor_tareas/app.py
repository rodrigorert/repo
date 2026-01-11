import json
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# --- DATOS EN MEMORIA ---
tareas = []
siguiente_id = 1

# --- PERSISTENCIA (GUARDAR Y CARGAR) ---
def guardar_datos():
    """Guarda las tareas y el ID actual en un archivo JSON."""
    global tareas, siguiente_id
    with open('tareas.json', 'w') as f:
        json.dump({'siguiente_id': siguiente_id, 'tareas': tareas}, f)

def cargar_datos():
    """Carga los datos del archivo JSON al iniciar el programa."""
    global tareas, siguiente_id
    try:
        with open('tareas.json', 'r') as f:
            data = json.load(f)
            tareas = data['tareas']
            siguiente_id = data['siguiente_id']
    except FileNotFoundError:
        # Si el archivo no existe (primera vez), iniciamos vacíos
        tareas = []
        siguiente_id = 1

# --- CARGAR DATOS AL INICIO ---
# Esto se ejecuta una sola vez cuando arrancas el programa
cargar_datos()

# --- FUNCIONES AUXILIARES ---
def agregar_tarea(texto):
    global siguiente_id
    tareas.append({'id': siguiente_id, 'texto': texto, 'hecho': False})
    siguiente_id += 1
    guardar_datos()  # <--- GUARDAMOS CADA VEZ QUE AGREGAMOS

def completar_tarea(id):
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['hecho'] = True
            break
    guardar_datos()  # <--- GUARDAMOS CADA VEZ QUE COMPLETAMOS

# --- RUTAS (VISTAS) ---
@app.route('/')
def index():
    tareas_ordenadas = sorted(tareas, key=lambda t: t['hecho'])
    return render_template('index.html', tareas=tareas_ordenadas)

@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect('/')

@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect('/')

# --- INICIO DEL SERVIDOR ---
if __name__ == '__main__':
    app.run(debug=True, port=5001)