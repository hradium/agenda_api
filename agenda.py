from flask import Flask, request, make_response, jsonify
import mysql.connector

from contactos import Contactos
conexion = mysql.connector.connect(user="carlos",password="12345",database="contactos")

cursor = conexion.cursor()

app = Flask(__name__)

@app.route("/contactos/", methods=['GET'])
def contactos():
	con = Contactos(conexion, cursor)
	resultado = con.buscar()
	print(resultado)
	
	return jsonify(resultado)
@app.route("/detalles/", methods=['GET'])
def detalles():
	id_contacto = request.args.get('id')
	det = Contactos(conexion, cursor)
	resultado = det.recuperar(id_contacto)
	print(resultado)
	
	return jsonify(resultado)
@app.route("/agregar/", methods=['GET'])
def login():
	#print(request.args)
	nombre=request.args.get('nombre')
	correo=request.args.get('correo')
	telefono=request.args.get('telefono')
	facebook=request.args.get('facebook')
	twitter=request.args.get('twitter')
	instagram=request.args.get('instagram')
	
	add = Contactos(conexion,cursor)
	respuesta=add.agregar(nombre,correo,telefono,facebook,twitter,instagram)
	#respuesta.headers.add('Access-Control-Allow-Origin','*')
	return jsonify(respuesta)
app.run(debug=True)

