import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='5360574',
                db='personas_bd'
            )
            if self.conexion.is_connected ():
                print ("Conexión exitosa.")
                cursor = self.conexion.cursor()
                cursor.execute ("SELECT database();")
                registro= cursor.fetchone()
                print("Conectado a :", registro)
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listaDeCursos(self):
        if self.conexion.is_connected():
            try:    
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM user")
                resultados = cursor.fetchall()
                print(resultados)
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
    def registrarCurso(self,curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO user (codigo, curso, creditos) VALUES ('{0}', '{1}', {2})"
                cursor.execute(sql.format(curso[0], curso[1], curso[2]))
                self.conexion.commit()
                print("¡Curso registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE user SET curso = '{0}', creditos = {1} WHERE codigo = '{2}'"
                cursor.execute(sql.format(curso[1], curso[2], curso[0]))
                self.conexion.commit()
                print("¡Curso actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarCurso(self, codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM user WHERE codigo = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print("¡Curso eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))