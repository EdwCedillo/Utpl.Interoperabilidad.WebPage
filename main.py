from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de personas
personaList = [{"nombre": "Juan", "apellido": "Perez", "edad": 25},
            {"nombre": "Ana", "apellido": "Gomez", "edad": 30},
            {"nombre": "Carlos", "apellido": "Lopez", "edad": 45}]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/personas')
def personas():
    return render_template('personas.html', personas=personaList)

@app.route('/personas', methods=['POST'])
def add():
    print("llego por aqui a guardar")
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    edad = int(request.form.get('edad'))

    personaList.append({"nombre": nombre, "apellido": apellido, "edad": edad})

    return redirect(url_for('personas'))

@app.route('/huespedes')
def huespedes():
    responseHabitaciones = requests.get('https://utpl-interoperabilidad-ejercicio1.onrender.com/v1_0/huesped')
    return render_template('huespedes.html', huespedesl=responseHabitaciones.json())

if __name__ == '__main__':
    app.run(debug=True)