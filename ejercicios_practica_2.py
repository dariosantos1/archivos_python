# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos
# Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion

import csv
from pickle import APPEND


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    csvfile = open('stock.csv')
    data = list(csv.DictReader(csvfile))
    cantidad_filas = len(data)
    sumatoria_tornillos = []
    suma = ()
    for i in range (cantidad_filas) :
        fila = data[i]
        try :
            tornillos = int(fila.get("tornillos"))
            sumatoria_tornillos.append(tornillos)
        except :
            print ("error")
    print ("La sumatoria de todos los tornilos es :" , sum(sumatoria_tornillos))

    csvfile.close()
    
    
    

def ej4():
    
    print('Ejercicios con archivos CSV 2º')
    archivo = "propiedades.csv"
    
    #prop = open ("propiedades.cvs") 
    #data = list(csv.DictReader(prop))
    #cantidad_filas = len(data)
    #deptos_2am = []
    #deptos_2am = []



    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    with open("propiedades.csv") as csvfile:
        archivo = list(csv.DictReader(csvfile))
        deptos_2amb = 0
        deptos_3amb = 0
        for i in archivo:
            try :
                if i["ambientes"] == "2":
                    deptos_2amb += 1
                elif i["ambientes"] == "3":
                    deptos_3amb += 1
            except :
                print ("No se encontraron departamentos de 2 ni 3 ambientes")

    print("La cantidad de deptos con 2 ambientes es: ", deptos_2amb)
    print("La cantidad de deptos con 2 ambientes es: ", deptos_3amb)

    


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
