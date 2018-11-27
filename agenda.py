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
app.run(debug=True)

