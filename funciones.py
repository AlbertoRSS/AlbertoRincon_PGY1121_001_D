import os
os.system("cls")
import time
from datetime import datetime
from random import randint,shuffle








def ingresar_datos():
    registro = []
    while True:
        tipo = input("Por favor ingrese el tipo de vehiculo\n")
        if len(tipo) >= 2 and len(tipo) <= 15:
            registro.append(tipo)
            break
        else:
            print("tipo de vehiculo errado")
    while True:
        patente = input("Ingrese la patente del vehiculo:\n")
        if len(patente) >= 5 and len(patente) <= 6:
            registro.append(patente)
            break
        else:
            print("La patente debe ser entre 5 y 6 caracteres")
    while True:
        marca = input("Ingrese la marca del vehiculo:\n")
        if len(marca) >= 2 and len(marca) <= 15:
            registro.append(marca)
            break
        else:
            print("La marca debe tener entre 2 y 15 caracteres")      
    while True:
        precio = int(input("Ingrese el precio del vehiculo:\n"))
        if precio > 4999999:
            registro.append(precio)
            break
        else:
            print("El precio minimo es de $5.000.000\n")
    while True:
        multas = input("Si el vehiculo tiene multas indique con: |'SI' o 'NO'|:\n")
        if multas.lower() in ["si","no"]:
            registro.append(multas)
            break
        else:
            print("Opcion invalida por favor indique con: |SI o NO|\n")
    while True:
        fecha_multa = input("Si el vehiculo tiene multas indique la fecha (dd/mm/yy) de lo contrario indique 'NO':\n")
        if len(fecha_multa) >= 2 and len(fecha_multa) <= 15:
            registro.append(fecha_multa)
            break
        else:
            print("Opcion invalida, indique la fecha (dd/mm/yy) o la opción 'NO' \n")
    while True:
        nom_dueño = input("Por favor ingrese el nombre del dueño del vehiculo:\n")
        if len(nom_dueño) >= 2 and len(nom_dueño) <= 25:
            registro.append(nom_dueño)
            break
        else:
            print("El nombre debe tener entre 2 y 25 caracteres")


    return registro


def burcar_registro(patente,registro_autos):


    patente = input("ingrese la patente del vehiculo:\n")
    encontrado = False
    for registro in registro_autos:
        if patente in registro:
            print(registro)
            encontrado = True
            break
    if encontrado is False:
        print("Registro no encontrado.")
       


def funcion_mezclar():
    valores = randint(1500,3500)
    return valores


def salir():
    print("Gracias por visitar La automotora “Auto Seguro” | Hasta pronto")
    time.sleep(3)
    os.system("cls")