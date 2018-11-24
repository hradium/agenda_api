class Contactos:
	def __init__(self, conexion, cursor):
		self.conexion = conexion
		self.cursor = cursor
		
	def agregar(self, nombre, correo, telefono, facebook, twitter, instagram):
		insertar=("INSERT INTO contacto(nombre, correo, telefono, facebook, twitter, instagram) VALUES(%s, %s, %s, %s, %s, %s)")
		
		self.cursor.execute(insertar, (nombre, correo, telefono, facebook, twitter, instagram))
		
		self.conexion.commit()
		
	def buscar(self):
		contactos = []
		select = ("SELECT * FROM contacto")
		self.cursor.execute(select,)
		for p in self.cursor.fetchall():
			contacto = {
				'id': p[0],
				'nombre': p[1],
				'correo': p[2],
				'telefono': p[3],
				'facebook': p[4],
				'twitter': p[5],
				'instagram': p[6]
			}
			contactos.append(contacto)
			
		return contactos