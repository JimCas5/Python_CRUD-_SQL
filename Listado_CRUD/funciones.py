def listarpersonas(listas):
    print(" ")
    print( 'Personas: ')
    cont = 1
    for pl in listas:
        datos= " {0}.codigo :{1}| Nombre:  {2} | CC: {3} | Edad: {4} " 
        print ( datos.format(pl[0],pl[1],pl[2],pl[3]))
        cont = cont + 1
    print ('')
    print ('')

def registrarpersona():
    codigo= input("Ingrese codigo : ")
    nombre= input("Ingrese nombre :")
    cedula = input ("Numero del celular :")
    telefono = int(input("Edad :"))
    datos = (codigo, nombre,cedula, telefono)
    return datos

def eliminardatos(listas):
    print('')
    existeCodigo= False
    codigoeliminar= input ("Codigo a eliminar: " )
    for pl in listas:
        if pl[0]==codigoeliminar:
            existeCodigo = True
            break
    return codigoeliminar

def pediractualizar(listas):
    print('')
    existe= False
    codigoeditar = input ("Ingrese codigo a editar: ")
    for cod in listas:
        if cod[0] ==codigoeditar:
            existe = True
            break
    if existe:
        nombre= input ("Ingrese nombre a modificar: ")
        cedula= input("Numero de cedula a modificar: ")
        celular= input("Edad a modificar")
    datos = (codigoeditar, nombre, cedula, celular)
    return datos






    
