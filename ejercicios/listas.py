suma = 1+1
resta = 3-2
multiplicar = 6 * 3
dividir = 6/3
es_par = lambda numero: numero % 2 == 0

#def es_par(numero):
#    return numero % 2 == 0

def es_impar(numero):
    return numero % 2 != 0

print(es_impar(130))
print(es_par(60))

numeros = [10,2,3]
numeros.append(5)
numeros.append(7)

print(f"Numeros: {numeros}")

jose = []
for x in range(1,11):
    jose.append(x)
print(f"numeros: {jose}")

#!/usr/bin/env python3

"""
Ejercicio 6: ¡Aprendiendo a usar bucles for!

Este ejercicio te ayudará a entender:
- Cómo usar bucles for para repetir acciones
- Cómo recorrer listas y rangos de números
- Cómo acumular resultados usando bucles
"""

def sumar_numeros(hasta):
    """
    TODO: Suma todos los números desde 1 hasta el número indicado.
    
    Por ejemplo:
    sumar_numeros(3) debe sumar: 1 + 2 + 3 = 6
    sumar_numeros(5) debe sumar: 1 + 2 + 3 + 4 + 5 = 15
    
    PISTA 1: Usa range(1, hasta + 1) para generar los números
    PISTA 2: Crea una variable total = 0 antes del bucle
    PISTA 3: En el bucle, suma cada número al total
    """
    pass  # Reemplaza esto con tu código

def contar_vocales(palabra):
    """
    TODO: Cuenta cuántas vocales (a,e,i,o,u) hay en una palabra.
    No importa si son mayúsculas o minúsculas.
    
    Por ejemplo:
    contar_vocales("Python") -> 1 (solo la 'o')
    contar_vocales("Ejercicio") -> 4 (e,e,i,o)
    
    PISTA 1: Convierte la palabra a minúsculas con .lower()
    PISTA 2: Crea una lista de vocales: vocales = ['a','e','i','o','u']
    PISTA 3: Usa un bucle for para revisar cada letra de la palabra
    PISTA 4: Si la letra está en la lista de vocales, súmala al contador
    """
    pass  # Reemplaza esto con tu código

def crear_tabla_multiplicar(numero):
    """
    TODO: Crea la tabla de multiplicar para un número (del 1 al 10).
    Debe retornar una lista con los resultados.
    
    Por ejemplo:
    crear_tabla_multiplicar(3) -> [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    
    PISTA 1: Crea una lista vacía para guardar los resultados
    PISTA 2: Usa range(1, 11) para multiplicar del 1 al 10
    PISTA 3: En cada vuelta del bucle, multiplica y guarda el resultado
    """
    
    tabla = []
    for x in range(1,11):
        resultado = numero * x
        tabla.append(resultado)
    return tabla

def encontrar_pares(numeros):
    """
    TODO: Encuentra todos los números pares en una lista.
    Debe retornar una nueva lista solo con los números pares.
    
    Por ejemplo:
    encontrar_pares([1, 2, 3, 4, 5, 6]) -> [2, 4, 6]
    
    PISTA 1: Crea una lista vacía para los números pares
    PISTA 2: Un número es par si numero % 2 == 0
    PISTA 3: Usa un bucle for para revisar cada número
    PISTA 4: Si el número es par, agrégalo a la lista
    """
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

def main():
    # Prueba 1: Sumar números
    print("=== Suma de Números ===")
    for n in [3, 5, 7]:
        resultado = sumar_numeros(n)
        print(f"La suma de los números hasta {n} es: {resultado}")
    
    # Prueba 2: Contar vocales
    print("\n=== Contando Vocales ===")
    palabras = ["Python", "Ejercicio", "Programacion", "Computadora"]
    for palabra in palabras:
        vocales = contar_vocales(palabra)
        print(f"'{palabra}' tiene {vocales} vocales")
    
    # Prueba 3: Tablas de multiplicar
    print("\n=== Tablas de Multiplicar ===")
    for n in [3, 5, 9, 12]:
        tabla = crear_tabla_multiplicar(n)
        print(f"Tabla del {n}: {tabla}")
    
    # Prueba 4: Encontrar números pares
    print("\n=== Buscando Números Pares ===")
    listas = [
        [1, 2, 3, 4, 5, 6],
        [10, 21, 34, 45, 58],
        [7, 11, 13, 17]
    ]
    for lista in listas:
        pares = encontrar_pares(lista)
        print(f"Números pares en {lista}: {pares}")

if __name__ == "__main__":
    main()


