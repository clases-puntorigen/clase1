#recorrer una lista
"""
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
"""

#ejercicio
nombres = ["Ana", "Carlos", "Elena", "Luis", "Marta"]
for nombre in nombres:
    print(nombre)

"""
ejemplo
for i in range(5):
    print("Hola, esta es la iteración número", i)
"""
#ejercicio
for x in range(11):
    print(x)

"""
for i in range(2, 11, 2):
    print(i)

Usa un for con range() para mostrar los números del 10 al 1, en orden descendente.
"""
#ejercicio

for numero in range(10,1,-1): #el 10 es el numero de cual empezar, el 1 es al numero que llegra, y el -1 indica que es en decadencia
    print(numero)

"""
Ejercicio 1: Números pares en un rango
Usa un for con range() para imprimir solo los números pares del 2 al 20.
"""
for numero in range(0,22,2):
    print(numero)

"""
Ejercicio 2: Suma de los primeros 10 números
Usa un for con range() para sumar los números del 1 al 10 e imprimir el resultado al final.
"""
suma = 0
for numero in range(10):
   suma += numero
   print(suma)
   