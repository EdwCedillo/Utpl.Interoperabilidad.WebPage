from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


#Declarar el API KEY generado de wso2 api manager desde la aplicacion
API_KEY = 'eyJ4NXQiOiJPREUzWTJaaE1UQmpNRE00WlRCbU1qQXlZemxpWVRJMllqUmhZVFpsT0dJeVptVXhOV0UzWVE9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbkBjYXJib24uc3VwZXIiLCJhcHBsaWNhdGlvbiI6eyJvd25lciI6ImFkbWluIiwidGllclF1b3RhVHlwZSI6bnVsbCwidGllciI6IlVubGltaXRlZCIsIm5hbWUiOiJhcHBfRWR3aW4iLCJpZCI6NiwidXVpZCI6ImRkMjVkMWIyLTRjZmEtNGQzZC1hN2Q2LTI0NjQ0ZWNiODVmZCJ9LCJpc3MiOiJodHRwczpcL1wvdXRwbHdzbzIudGs6NDQzXC9hcGltXC9vYXV0aDJcL3Rva2VuIiwidGllckluZm8iOnsiVW5saW1pdGVkIjp7InRpZXJRdW90YVR5cGUiOiJyZXF1ZXN0Q291bnQiLCJncmFwaFFMTWF4Q29tcGxleGl0eSI6MCwiZ3JhcGhRTE1heERlcHRoIjowLCJzdG9wT25RdW90YVJlYWNoIjp0cnVlLCJzcGlrZUFycmVzdExpbWl0IjowLCJzcGlrZUFycmVzdFVuaXQiOm51bGx9fSwia2V5dHlwZSI6IlNBTkRCT1giLCJwZXJtaXR0ZWRSZWZlcmVyIjoiIiwic3Vic2NyaWJlZEFQSXMiOlt7InN1YnNjcmliZXJUZW5hbnREb21haW4iOiJjYXJib24uc3VwZXIiLCJuYW1lIjoiVXRwbFBlcnNvbmFzIiwiY29udGV4dCI6IlwvYXBpcGVyc29uYVwvMy4wIiwicHVibGlzaGVyIjoiYWRtaW4iLCJ2ZXJzaW9uIjoiMy4wIiwic3Vic2NyaXB0aW9uVGllciI6IlVubGltaXRlZCJ9LHsic3Vic2NyaWJlclRlbmFudERvbWFpbiI6ImNhcmJvbi5zdXBlciIsIm5hbWUiOiJVdHBsLUVEVy1DbGllbnRlIiwiY29udGV4dCI6IlwvYXBpLUNsaWVudGVcLzEuMCIsInB1Ymxpc2hlciI6ImFkbWluIiwidmVyc2lvbiI6IjEuMCIsInN1YnNjcmlwdGlvblRpZXIiOiJVbmxpbWl0ZWQifV0sInRva2VuX3R5cGUiOiJhcGlLZXkiLCJwZXJtaXR0ZWRJUCI6IiIsImlhdCI6MTY5MDc2MzAxMiwianRpIjoiZDM0MGJiNWQtNGM4YS00ZDk2LWE0OWEtZWEzYmUyOGIwM2NjIn0=.scC0lPk8Vz94GBe3V1FicPnGrTFrAA5CqvrJ79v4uWJHoFlC9t0J902mRQPjODJj_fhl9OmYyekfcJpIGwhFS2vDYpTfbUB4HqPEP4Jts_7GIGIjuTRRkAr-pBqxmWjskVt-jIX0rNOtzMSa6FXdUPv1vhIQWbdqKrs-RzZ__x-g7y4k9YqwdGJtMa1KFa4PM8r1kBhD7e_o1VO3u22LseECuiVw3sITvfp-E2_FBOvnKV1IuuuotAdetCY7WdxYaRtGQdk6OQLV_OtS8N7MnDFHEGrXuGiBsginIYvbq8MkXeUxJOYuHBJHZ0RPS2SZFy6weAa4VOoSR8OQsI4Z1g=='

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

#modificar a futuro
@app.route('/personas')
def personas():
    #prox tuto
    headers = {'apikey': API_KEY}
    response = requests.get('https://utplwso2.tk/apipersona/3.0/personas', headers=headers)
    #print(response)
    return render_template('personas.html', personas=response.json())
    #return render_template('personas.html', personas=personaList)

#editar esta parte
@app.route('/personas/delete/<idpersona>')
def delete_personas(idpersona):
    headers = {'apikey': API_KEY}
    response = requests.delete('https://utplwso2.tk/apipersona/3.0/personas/'+idpersona, headers=headers)
    print(response)
    return redirect(url_for('personas'))

@app.route('/personas', methods=['POST'])
def add():
    print("llego por aqui a guardar")
    nombre = request.form.get('nombre')
    identificacion = request.form.get('identificacion')
    edad = int(request.form.get('edad'))
    ciudad = request.form.get('ciudad')


    person_data = {"nombre": nombre, "edad": edad, "ciudad": ciudad, "identificacion": identificacion}

    headers = {'apikey': API_KEY}
    responseHabitacionesS = requests.post('https://utplwso2.tk/apipersona/3.0/personas', json=person_data, headers=headers)

    return redirect(url_for('personas'))

@app.route('/huespedes')
def huespedes():
    responseHabitaciones = requests.get('https://utpl-interoperabilidad-ejercicio1.onrender.com/v1_0/huesped')
    return render_template('huespedes.html', huespedesl=responseHabitaciones.json())


@app.route('/huespedes', methods=['POST'])
def addHuesped():
    print("llego por aqui a guardar huespedes")

    nombreValue = request.form.get('nombre')
    ciudad = request.form.get('ciudad')
    edad = int(request.form.get('edad'))
    hab = int(request.form.get('hab'))

    room_data = {
        "nombre": nombreValue,
        "ciudad": ciudad,
        "edad": edad,
        "hab": hab
    }

    responseHabitacionesS = requests.post('https://utpl-interoperabilidad-ejercicio1.onrender.com/v1_0/huesped', json=room_data)

    return redirect(url_for('huespedes'))


if __name__ == '__main__':
    app.run(debug=True)