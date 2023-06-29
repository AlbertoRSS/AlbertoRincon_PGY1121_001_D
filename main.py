import os
import time
from funciones import *
from random import randint,shuffle
os.system("cls")




print("Bienvenido a la automotora “Auto Seguro” ")
time.sleep(2)
os.system("cls")








dueño_certificado = ["Alberto Segredo","Pablo Rodriguez","Jose Bustamante"]
nombre_certificado = ["Vehiculo","Moto","Camionetas"]
patente = ["XXLH87","RPLG55","LHRF44"]
registro_autos = []
iterar = True
while iterar == True:
    seleccion = input("""
Ingrese una opcion del menu:








1) Guardar datos de un vehiculo
2) Buscar datos de un vehiculo
3) Imprimir "certificados de Emisión de contaminantes"
4)Salir del menu\n""")
    if seleccion == "1":
        registro_autos.append(ingresar_datos())
        print("Datos ingresados correctamente\n\nVolviendo al menu principal")
        time.sleep(2)
        os.system("cls")
    elif seleccion == "2":
        patente = input("ingrese la patente del vehiculo:\n")
        os.system("cls")
        encontrado = False
        for registro in registro_autos:
            if patente in registro:
                print("-------Buscando la patente--------")
                time.sleep(2)
                os.system("cls")
                print(registro_autos)
                time.sleep(20)
                encontrado = True
                break
        if encontrado is False:
            print("Registro no encontrado.")
            time.sleep(2)
            iterar = True
    elif seleccion == "3":
        break                  
    elif seleccion == "4":
        salir()
        break
    else:
        print("Error al ingresar la opcion")
        time.sleep(1)
        os.system("cls")
        iterar = True


if seleccion == "3":
    print("Imprimiendo su certificado\n")
    time.sleep(2)
    os.system("cls")
    print("------------------")
    print("Nombre:")        
    shuffle(dueño_certificado)
    print(dueño_certificado[0])
    print("Tipor de certificado:")
    shuffle(nombre_certificado)
    print(nombre_certificado[0])
    print("Patente:")
    shuffle(patente)
    print(patente[0])
    print("------------------")
    print("Precio a pagar:\n")
    print(funcion_mezclar())