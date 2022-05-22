from flask import Flask, jsonify, render_template, request
from dbmysql import DBMySQL
#python -m flask run
#set FLASK_APP=server.py

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/formfind') #Formulario para encontrar un dato
def formularioEncontrar():
    return render_template('encontrar.html')

@app.route('/formfind/find' , methods=('GET', 'POST')) #Ejecuta la busqueda y retorna el dato encontrado
def encontrado():
    db = DBMySQL() 
    codigo = request.form['codef']
    resultado = db.findByCodeCountry(codigo)
    db.closeConnection()
    return render_template('mostrar.html', countrys=resultado ) + " <a href='/'> <button>Regresar al Inicio</button>"

@app.route('/mostrardatos') #Muestra todos los datos de la base de datos
def mostrarDatos():
    db = DBMySQL() 
    resultado = db.getAllCountrys()
    return render_template('mostrar.html', countrys=resultado ) + " <a href='/'> <button>Regresar al Inicio</button>"

@app.route('/formactualizar') #Formulario para actualizar los datos
def formularioActualizar():
    return render_template('actualizar.html')

@app.route('/formactualizar/actualizar', methods=['POST']) #Eejecuta la actualizacion y retorna el dato actualizado
def actualizar():
    db = DBMySQL() 
    codigo = request.form['codea']
    nombre = request.form['namea']
    continente = request.form['continenta']
    region = request.form['regiona']
    surfacearea = request.form['surfaceAreaa']
    indepyear = request.form['indepYeara']
    population = request.form['populationa']
    lifeexpectancy = request.form['lifeExpectancya']
    gnp = request.form['gnpa']
    gnpold = request.form['gnpOlda']
    localname = request.form['localNamea']
    governmentform = request.form['governmentForma']
    headofstate = request.form['headOfStatea']
    capital = request.form['capitala']
    code2 = request.form['code2a']
    db.actualizarCountry(codigo, nombre, continente, region, surfacearea, indepyear, population, lifeexpectancy, gnp, gnpold, localname, governmentform, headofstate, capital, code2)
    resultado = db.findByCodeCountry(codigo)
    db.closeConnection()
    return render_template('mostrar.html', countrys=resultado) + "<a href='/'> <button>Regresar al Inicio</button>"

@app.route('/formingresar') #Formulario para ingresar un dato
def formularioIngresar():
    return render_template('ingresar.html')

@app.route('/formingresar/ingresar', methods=['POST']) #Ejecuta el ingreso del dato y retorna el dato ingresado
def ingresar():
    db = DBMySQL() 
    codigo = request.form['code']
    nombre = request.form['name']
    continente = request.form['continent']
    region = request.form['region']
    surfacearea = request.form['surfaceArea']
    indepyear = request.form['indepYear']
    population = request.form['population']
    lifeexpectancy = request.form['lifeExpectancy']
    gnp = request.form['gnp']
    gnpold = request.form['gnpOld']
    localname = request.form['localName']
    governmentform = request.form['governmentForm']
    headofstate = request.form['headOfState']
    capital = request.form['capital']
    code2 = request.form['code2']
    db.insertarCountry(codigo, nombre, continente, region, surfacearea, indepyear, population, lifeexpectancy, gnp, gnpold, localname, governmentform, headofstate, capital, code2)
    resultado = db.findByCodeCountry(codigo)
    db.closeConnection()
    return render_template('mostrar.html', countrys=resultado) + "<a href='/'> <button>Regresar al Inicio</button>"

@app.route('/formeliminar') #Formulario para eliminar un dato
def formularioEliminar():
    return render_template('eliminar.html')

@app.route('/formeliminar/eliminar' , methods=('GET', 'POST')) #Ejecuta la eliminacion y retorna todos los datos de la base de datos
def eliminado():
    db = DBMySQL() 
    codigo = request.form['codee']
    db.eliminarByCodeCountry(codigo)
    resultado = db.getAllCountrys()
    db.closeConnection()
    return render_template('mostrar.html', countrys=resultado) + "<a href='/'> <button>Regresar al Inicio</button>"
