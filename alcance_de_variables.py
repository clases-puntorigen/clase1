#!/usr/bin/env python3

"""
Ejercicio 3: Alcance de Variables y Contextos

Este ejercicio te ayudará a entender:
- Variables globales y locales
- Contextos de funciones
- Modificación de variables en diferentes contextos
- La palabra clave 'global'
- Ámbito de variables en funciones anidadas
"""

# Variable global de ejemplo
contador = 0

def incrementar_contador():
    """
    TODO: Modifica esta función para que:
    1. Use la variable global 'contador'
    2. Incremente su valor en 1
    3. Retorne el nuevo valor
    
    
    Pista: Necesitarás usar la palabra clave 'global'
    """
    global contador
    contador = contador + 1
    #contador += 1
    return contador


def crear_multiplicador(factor):
    """
    TODO: Completa esta función que:
    1. Recibe un factor como parámetro
    2. Define una función interna 'multiplicar' que multiplica un número por el factor
    3. Retorna la función interna
    
    Ejemplo de uso:
    duplicar = crear_multiplicador(2)
    duplicar(5) -> retorna 10
    """
    
    def multiplicar(num):
        return num * factor
    
    return multiplicar


def calcular_suma():
    """
    TODO: Completa esta función que demuestre el alcance de variables:
    1. Crea una variable 'total' con valor inicial 0
    2. Define una función interna 'agregar' que:
       - Recibe un número
       - Actualiza 'total' sumándole ese número
       - Retorna el nuevo total
    3. Retorna la función 'agregar'
    
    Ejemplo de uso:
    sumador = calcular_suma()
    sumador(5) -> retorna 5
    sumador(3) -> retorna 8
    """
    total = 0
    def agregar(numero):
        nonlocal total
        total += numero
        return total
    
    return agregar

def main():
    # Prueba de incrementar_contador
    print(f"Contador inicial: {contador}")
    for _ in range(3):
        nuevo_valor = incrementar_contador()
        print(f"Nuevo valor del contador: {nuevo_valor}")
    
    # Prueba de crear_multiplicador
    duplicar = crear_multiplicador(2)
    triplicar = crear_multiplicador(3)
    numero = 5
    print(f"\nProbando multiplicadores con {numero}:")
    print(f"Duplicar: {duplicar(numero)}")
    print(f"Triplicar: {triplicar(numero)}")
    
    # Prueba de calcular_suma
    sumador = calcular_suma()
    print("\nProbando sumador:")
    print(f"Agregar 5: {sumador(5)}")
    print(f"Agregar 3: {sumador(3)}")
    print(f"Agregar 2: {sumador(2)}")
    print(f"Agregar 90: {sumador(90)}")

if __name__ == "__main__":
    main()
