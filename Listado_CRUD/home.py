from Base.conexion import BASE
import funciones


def Principal():
    continuar= True
    while(continuar):
        correcta= False
        while( not correcta): 
            print('========< MENU >===========')
            print(' 1) Listar Personas')
            print(' 2) Registrar Personas')
            print(' 3) Actualizar Personas')
            print(' 4) Eliminar Personas')
            print(' 5) Salir')
            print('===========================')

            opcion= int(input("Seleccione una opción: "))
            if opcion <1 or opcion>5:
                print('Opcion incorrecta, Intente nuevamente')
            elif opcion ==5 :
                continuar = False
                print('Salio de la app\n')
                break
            else:
                correcta = True
                ejecutar(opcion)
                

def ejecutar(opcion):
    data = BASE()
    #Estructrura
    #R
    if opcion== 1:
        try:
            listas = data.Listarpersonas()
            print("________________")
            print("________________")
        except:
                print ('Error al intentar la conexión: ' )                

    #C
    elif opcion == 2: 
        try :
            listas= funciones.registrarpersona()
            data.registrarpersona(listas)
        except:
            print ("Ocurrio un error ...")                
    
    #U
    elif opcion == 3:
        try:
            listas = funciones.pediractualizar() 
            if listas:
                data.Listarpersonas(listas)
            else:
                print ("Codigo a actualizar no encontrado\n")
        except: 
            print("Error...")

    #D    
    elif opcion == 4:
        try:
            listas= data.Listarpersonas()
            codigoeliminar= funciones.eliminardatos(listas)
            if not (codigoeliminar == " "):
                data.eliminarpersona(codigoeliminar)
            else:
                print("Codigo no encontrado... ")
        except:
            print ("Ocurrio un error ...")                
    else:
        print ("Invalido")
    

Principal ()

    