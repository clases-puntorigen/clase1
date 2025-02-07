#!/usr/bin/env python3

"""
Solución: Comprensión de Listas y Diccionarios en Python

Este ejercicio te ayudará a entender:
- Cómo usar 'for' e 'if' en una sola línea
- Cómo crear listas usando comprensión de listas
- Cómo crear diccionarios usando comprensión de diccionarios
- Cómo transformar datos de forma concisa y elegante
"""

# Datos de ejemplo para trabajar
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
palabras = ["casa", "perro", "gato", "elefante", "mariposa"]
precios = {"manzana": 890, "pera": 750, "naranja": 690, "uva": 990}

def obtener_numeros_pares(numeros):
    """
    Usa comprensión de listas para obtener solo los números pares
    """
    return [n for n in numeros if n % 2 == 0]

def obtener_palabras_largas(palabras, longitud_minima):
    """
    Usa comprensión de listas para obtener palabras más largas que longitud_minima
    """
    return [palabra for palabra in palabras if len(palabra) > longitud_minima]

def obtener_cuadrados(numeros):
    """
    Usa comprensión de listas para obtener el cuadrado de cada número
    """
    return [n * n for n in numeros]

def crear_diccionario_longitudes(palabras):
    """
    Usa comprensión de diccionarios para crear un diccionario de longitudes
    """
    return {palabra: len(palabra) for palabra in palabras}

def aplicar_descuento(precios, porcentaje):
    """
    Usa comprensión de diccionarios para aplicar un descuento a los precios
    """
    return {item: precio * ((100 - porcentaje) / 100) for item, precio in precios.items()}

def test_obtener_numeros_pares():
    nums = [1, 2, 3, 4, 5, 6]
    assert obtener_numeros_pares(nums) == [2, 4, 6]

def test_obtener_palabras_largas():
    palabras_test = ["sol", "luna", "estrella", "mar"]
    assert obtener_palabras_largas(palabras_test, 4) == ["luna", "estrella"]

def test_obtener_cuadrados():
    nums = [1, 2, 3]
    assert obtener_cuadrados(nums) == [1, 4, 9]

def test_crear_diccionario_longitudes():
    palabras_test = ["sol", "luna"]
    assert crear_diccionario_longitudes(palabras_test) == {"sol": 3, "luna": 4}

def test_aplicar_descuento():
    precios_test = {"a": 100, "b": 200}
    assert aplicar_descuento(precios_test, 20) == {"a": 80.0, "b": 160.0}

def main():
    print("=== Comprensión de Listas y Diccionarios ===")
    
    # Probar números pares
    pares = obtener_numeros_pares(numeros)
    print("\nNúmeros pares:", pares)
    
    # Probar palabras largas
    largas = obtener_palabras_largas(palabras, 5)
    print("\nPalabras con más de 5 letras:", largas)
    
    # Probar cuadrados
    cuadrados = obtener_cuadrados(numeros)
    print("\nCuadrados de los números:", cuadrados)
    
    # Probar diccionario de longitudes
    longitudes = crear_diccionario_longitudes(palabras)
    print("\nLongitud de cada palabra:")
    for palabra, longitud in longitudes.items():
        print(f"{palabra}: {longitud} letras")
    
    # Probar descuentos
    descuentos = aplicar_descuento(precios, 20)
    print("\nPrecios con 20% de descuento:")
    for producto, precio in descuentos.items():
        print(f"{producto}: ${precio}")

    # Ejecutar pruebas
    test_obtener_numeros_pares()
    test_obtener_palabras_largas()
    test_obtener_cuadrados()
    test_crear_diccionario_longitudes()
    test_aplicar_descuento()
    print("\n¡Todas las pruebas pasaron exitosamente!")

if __name__ == "__main__":
    main()
