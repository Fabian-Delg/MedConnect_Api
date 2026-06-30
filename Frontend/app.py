from flask import Flask, render_template, request, redirect, url_for
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

API_CITAS = 'http://localhost:8000/api/citas/'
API_PACIENTES = "http://localhost:8000/api/pacientes/"
API_MEDICOS = "http://localhost:8000/api/medicos/"
USERNAME = 'admin'
PASSWORD = 'admin12345'

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

# Punto de entrada principal de la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=5000)
