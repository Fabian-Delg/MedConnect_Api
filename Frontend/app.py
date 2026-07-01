from flask import Flask, render_template, request, redirect, url_for, session
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
app.secret_key = "medconnect"

API_CITAS = 'http://localhost:8000/api/citas/'
API_PACIENTES = "http://localhost:8000/api/pacientes/"
API_MEDICOS = "http://localhost:8000/api/medicos/"
API_RECETAS = "http://localhost:8000/api/recetas/"
API_LOGIN = "http://localhost:8000/api/login/"
API_REGISTRO = "http://localhost:8000/api/registro/"
USERNAME = 'admin'
PASSWORD = 'admin12345'

# Cita
@app.route('/citas')
def lista_citas():
    response = requests.get(API_CITAS, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    citas = response.json()
    return render_template('cita/lista.html', citas = citas)

@app.route('/citas/crear', methods=['GET','POST'])
def crear_cita():
    if request.method == 'POST':
        data = {
            'paciente': request.form.get('paciente'),
            'medico': request.form.get('medico'),
            'fecha_cita': request.form['fecha_cita'],
            'hora_inicio': request.form['hora_inicio'],
            'motivo_consulta': request.form['motivo_consulta'],
            'presion_arterial': request.form['presion_arterial'],
            'peso_kg': request.form['peso_kg'],
            'temperatura': request.form['temperatura'],
            'estado_cita': request.form['estado_cita']
        }
        requests.post(API_CITAS, json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        return redirect(url_for('lista_citas'))
    
    pacientes = requests.get(API_PACIENTES, auth=HTTPBasicAuth(USERNAME, PASSWORD)).json()
    medicos = requests.get(API_MEDICOS, auth=HTTPBasicAuth(USERNAME, PASSWORD)).json()

    return render_template(
        'cita/formulario.html',
        pacientes=pacientes,
        medicos=medicos
    )

@app.route('/citas/detalle/<int:id>')
def detalle_cita(id):
    url = f"{API_CITAS}{id}/"
    response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))

    if response.status_code == 200:
        cita = response.json()
        return render_template('cita/detalle.html', cita=cita)

    return "Cita no encontrada", 404

@app.route('/citas/editar/<int:id>', methods=['GET','POST'])
def editar_cita(id):
    url = f"{API_CITAS}{id}/"
    if request.method == 'POST':
        data = {
            'paciente': request.form.get('paciente'),
            'medico': request.form.get('medico'),
            'fecha_cita': request.form['fecha_cita'],
            'hora_inicio': request.form['hora_inicio'],
            'motivo_consulta': request.form['motivo_consulta'],
            'presion_arterial': request.form['presion_arterial'],
            'peso_kg': request.form['peso_kg'],
            'temperatura': request.form['temperatura'],
            'estado_cita': request.form['estado_cita']
        }
        requests.put(url, json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        return redirect(url_for('lista_citas'))
    
    pacientes = requests.get(API_PACIENTES, auth=HTTPBasicAuth(USERNAME, PASSWORD)).json()
    medicos = requests.get(API_MEDICOS, auth=HTTPBasicAuth(USERNAME, PASSWORD)).json()
    cita = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD)).json()
    
    return render_template('cita/formulario.html', cita=cita, pacientes=pacientes, medicos=medicos)

@app.route('/citas/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_cita(id):
    url = f"{API_CITAS}{id}/"

    if request.method == 'POST':
        requests.delete(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        return redirect(url_for('lista_citas'))

    cita = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD)).json()
    return render_template('cita/eliminar.html', cita=cita)

# Receta
@app.route('/recetas')
def lista_recetas():
    response = requests.get(API_RECETAS, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    recetas = response.json()
    return render_template('recetas/lista.html', recetas = recetas)

@app.route('/recetas/crear', methods=['GET','POST'])
def crear_receta():
    if request.method == 'POST':
        data = {
            'cita': request.form.get('cita'),
            'medicamento_principal': request.form.get('medicamento_principal'),
            'dosis_recomendada': request.form.get('dosis_recomendada'),
            'frecuencia_consumo': request.form['frecuencia_consumo'],
            'duracion_tratamiento': request.form['duracion_tratamiento'],
            'indicaciones_especiales': request.form['indicaciones_especiales'],
            'via_administracion': request.form['via_administracion'],
            'fecha_emision': request.form['fecha_emision'],
            'requiere_control': request.form.get('requiere_control') == 'true'
        }
        requests.post(API_RECETAS, json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        return redirect(url_for('lista_recetas'))
    citas = requests.get(API_CITAS, auth=HTTPBasicAuth(USERNAME, PASSWORD)).json()
    return render_template('recetas/form.html', citas=citas)

@app.route('/recetas/editar/<int:id>', methods=['GET','POST'])
def editar_receta(id):
    url = f"{API_RECETAS}{id}/"
    if request.method == 'POST':
        data = {
            'cita': request.form.get('cita'),
            'medicamento_principal': request.form.get('medicamento_principal'),
            'dosis_recomendada': request.form.get('dosis_recomendada'),
            'frecuencia_consumo': request.form['frecuencia_consumo'],
            'duracion_tratamiento': request.form['duracion_tratamiento'],
            'indicaciones_especiales': request.form['indicaciones_especiales'],
            'via_administracion': request.form['via_administracion'],
            'fecha_emision': request.form['fecha_emision'],
            'requiere_control': request.form.get('requiere_control') == 'true'
        }
        requests.put(url, json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        return redirect(url_for('lista_recetas'))
    receta = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD)).json()
    citas = requests.get(API_CITAS, auth=HTTPBasicAuth(USERNAME, PASSWORD)).json()
    return render_template('recetas/form.html', receta=receta, citas=citas)

@app.route('/recetas/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_receta(id):
    url = f"{API_RECETAS}{id}/"

    if request.method == 'POST':
        requests.delete(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        return redirect(url_for('lista_recetas'))

    receta = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD)).json()
    return render_template('recetas/eliminar.html', receta=receta) 

# Login
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        data = {
            "username": request.form['username'],
            "password": request.form['password']
        }

        response = requests.post(API_LOGIN, json=data)

        if response.status_code == 200:
            session['usuario'] = data['username']
            return redirect(url_for('lista_citas'))

        return render_template(
            'base/login.html',
            error="Usuario o contraseña incorrectos"
        )

    return render_template('base/login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():

    if request.method == 'POST':

        data = {
            "username": request.form['username'],
            "email": request.form['email'],
            "password": request.form['password']
        }

        response = requests.post(API_REGISTRO, json=data)

        if response.status_code == 200:
            return redirect(url_for('login'))

        return render_template(
            'base/registro.html',
            error="No se pudo registrar el usuario"
        )

    return render_template('base/registro.html')

@app.route('/logout')
def logout():

    session.pop('usuario', None)

    return redirect(url_for('login'))

# Punto de entrada principal de la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=5000)
