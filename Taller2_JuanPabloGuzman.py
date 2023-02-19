"""
'''
Se tiene un censo de 500_000 registros.

cada registro tiene la siguiente estructura:

[numero de identificacion - nombre - edad - impuestos]

Los numeros de identificacion están ordenados ascendentemente y crecen de manera aleatoria en 1 o 2 unidades.
El nombre corresponde a una cadena de 5 caracteres del alfabeto tomados de manera aleatoria.
La edad es un numero aleatorio dentro de un rango de 18 a 99.
El impuesto es un bool que se toma aleatoriamente de la lista: True, True, True, False.

Crear un menu para realizar busquedas por numero y por nombre y mostrar en pantalla el resultado.

Una vez validado el programa.
Realizar la comparacion de complejidad entre ambas funciones a traves de una grafica en donde los datos de entrada (registros) incremente en un factor de 5:
1er censo: 500_000 registros
2ndo censo: 2_500_000 registros
3er censo: 12_500_000 registros
4to censo: 62_500_000 registros
5to censo: 312_500_000 registros
...

"""

import random
import time
import pandas as pd
import matplotlib.pyplot as plt

censo = []
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numero = 0
tamano = 500000

print("Creando censo ...")

for i in range(tamano):
    aumento = random.randint(1,2)
    numero += aumento

    letras = random.sample(alfabeto, 5)
    nombre = "".join(letras)

    edad = random.randint(18, 99)

    impuestos = random.choice((True, True, True, False))

    censo.append([numero, nombre, edad, impuestos])

    if len(censo) % 100000 == 0:
        print("Creados", len(censo), "registros")

print("Censo creado.")
print("ultimo registro: ", censo[-1])

def busqueda_numero(num):

    start=0
    end=len(censo)-1

    while start <= end:
        middle = (start+end) //2
        if censo[middle][0] == num:
            return middle
        elif num < censo[middle][0]:
            end = middle - 1
        else:
            start = middle + 1
    return None

def busqueda_nombre(censo, nom):

    for i in range(len(censo)):
        if censo[i][1] == nom:
            return i
    return None

def mostrar_registro(registro):

    print("Registro:")
    print([censo[registro][0], censo[registro][1], censo[registro][2], censo[registro][3]])

def menu():

    df = pd.DataFrame(columns=['n', 'numero', 'nombre'])
    n = []
    numero = []
    nombre = []
    seguir = True
    tiempos = []
    tamano2 = 500000

    while seguir == True:

        print("-----------------------------")
        print(" -- Censo de poblacion --")
        print("-----------------------------")
        print("1. Buscar por numero")
        print("2. Buscar por nombre")
        print("3. Mostrar grafica")
        print("4. Salir")
        opcion= input()

        if opcion == "1":
            print("Ingrese el numero que quiere buscar")
            num = int(input())
            for i in range (5):
                t0 = time.perf_counter()
                registro = busqueda_numero(num)
                t1 = time.perf_counter()
                tiempos.append(t1-t0)
                numero.append(t1 - t0)
                n.append(tamano2)
                tamano2 *= 5
            if registro is None:
                print("No se encontro el registro")
            else:
                mostrar_registro(registro)

        if opcion == "2":
            print("Ingrese el nombre que quiere buscar")
            nom = input()
            for i in range (5):
                t2 = time.perf_counter()
                registro = busqueda_nombre(censo, nom)
                t3 = time.perf_counter()
                tiempos.append(t3 - t2)
                nombre.append(t3 - t2)
            if registro is None:
                print("No se encontro el registro")
            else:
                mostrar_registro(registro)

        if opcion =="3":
            print("Tiempos de busqueda")
            print("Busqueda por numero:", tiempos[0])
            print("Busqueda por nombre:", tiempos[1])
            print()

            df['n'] = n
            df['numero'] = numero
            df['nombre'] = nombre

            print(df)
            df.plot(x='n', y=['numero' , 'nombre'])
            plt.grid()
            plt.show()

        if opcion == "4":
            seguir=False
            break

def main():
    menu()

if __name__ == "__main__":
    main()
    
    
    
    
    

