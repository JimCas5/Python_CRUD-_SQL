import mysql.connector
from mysql.connector import Error


#Conexion a la base de datos y listado 
 
class BASE():
    
    def __init__(self):
        try:
            self.conexion=mysql.connector.Connect (
                host='localhost',
                port= 3306,
                user='root',
                password='5360574',
                db='personas_bd',
            )

            if self.conexion.is_connected():
                print("Conexión exitosa")
                cursor=self.conexion.cursor()
                cursor.execute("SELECT database();")
                registro=cursor.fetchone()
                print("Conectado a :", registro)
        except Error as ex:
            print('Error al intentar la conexión: {0}'.format(ex) )

#Listado 
    def Listarpersonas(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM listado ") #ordenar de forma ascendente
                resultados= cursor.fetchall()
                print(resultados)
                return resultados
            except Error as ex:
                print ('Error al intentar la conexión: {0}'.format(ex) )

#Crear
    def registrarpersona (self,people):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql= "INSERT INTO listado (CODIGO, NOMBRE, CEDULA, CELULAR) VALUES ('{0}, {1},{2},{3})"
                cursor.execute (sql.format (people[0],people[1],people[2],people[3]))
                self.conexion.commit ()
                print("Persona Registrada!!\n ")
            except Error as ex:
                print ('Error al intentar la conexión: {0}'.format(ex) )

#eliminar
    def eliminarpersona(self, codigoeliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql="DELETE FROM listado WHERE codigo = '{0}'"
                cursor.execute (sql.format(codigoeliminar))
                self.conexion.commit()
                print("¡Persona eliminada!\n")
            except Error as ex:
                print ("Error en la conexión ")
#actualizar

    def actualizarcurso(self,people):
         if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql= "UPDATE listado SET codigo='{0}', Nombre '{1}', Cedula '{2}', celular{3}"
                cursor.execute (sql.format (people[0],people[1], people[2], people[3]))
                self.conexion.commit ()
                print("Actualizada \n ")
            except Error as ex:
                print ('Error al intentar la conexión: {0}'.format(ex) )






