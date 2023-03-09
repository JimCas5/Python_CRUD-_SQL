def listarCursos(cursos):
    print('____________')
    print(' ')
    print("Cursos: ")
    contador = 1
    for cur in cursos:
        datos = "{0}. Código: {1} | Nombre: {2} ({3} créditos)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print("___________")

def pedirDatos():
    codigoCorrecto = False

    while ( not codigoCorrecto):
       codigo= input("Ingrese codigo:  ")
       if len(codigo)==6:
           codigoCorrecto = True
       else:
           print ("Codigo debe ser de 6 digitos")
           
    nombre = input("Ingrese nombre: ")
    creditos= input("Creditos de Materia: ")

    curso= (codigo,nombre,creditos)
    return curso
    
def pedirDatosActualizacion(cursos):
    print("_______________")
    existeCodigo = False
    codigoEditar = input("Ingrese el código del curso a editar: ")
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        nombre = input("Ingrese nombre a modificar: ")

        creditosCorrecto = False
        while(not creditosCorrecto):
            creditos = input("Ingrese créditos a modificar: ")
        curso = (codigoEditar, nombre, creditos)
    else:
        curso = None

    return curso


def pedirDatosEliminacion(cursos):
    print("_______________")
    existeCodigo = False
    codigoEliminar = input("Ingrese el código del curso a eliminar: ")
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    return codigoEliminar


   