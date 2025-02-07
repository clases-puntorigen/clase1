#!/usr/bin/env python3

"""
Ejercicio: Comprensión de Listas y Diccionarios en Python

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
    TODO: Implementa una función que use comprensión de listas para obtener
    solo los números pares de la lista
    Ejemplo: [2, 4, 6, 8, 10]
    """
    #n = []
    #for numero in numeros:
    #    if numero % 2 == 0:
    #        n.append[numero]
    #return n
    return [n for n in numeros if n % 2 == 0]

def obtener_palabras_largas(palabras, longitud_minima):
    """
    TODO: Implementa una función que use comprensión de listas para obtener
    las palabras que tengan más de longitud_minima caracteres
    Ejemplo: para longitud_minima=4 -> ["casa", "perro", "elefante", "mariposa"]
    """
    #largas = []
    #for palabra in palabras:
    #    if len(palabra) > longitud_minima:
    #        largas.append(palabra)
    #return largas
    return [palabra for palabra in palabras if len(palabra) > longitud_minima]

def obtener_cuadrados(numeros):
    """
    TODO: Implementa una función que use comprensión de listas para obtener
    una lista con el cuadrado de cada número
    Ejemplo: [1, 4, 9, 16, 25, ...]
    return [1*1, 4*4, 9*9, 16*16, 25*25, ...]
    """
    return [numero * numero for numero in numeros]

def crear_diccionario_longitudes(palabras):
    """
    TODO: Implementa una función que use comprensión de diccionarios (objeto) para crear
    un diccionario donde la llave sea la palabra y el valor su longitud
    Ejemplo: {"casa": 4, "perro": 5, ...}
    palabras = ["casa", "perro", "gato", "elefante", "mariposa"]
    return {
        "casa": 4,
        "perro": 5,
        "gato": 4,
        etc..
    }
    """
    return {palabra: len(palabra) for palabra in palabras}
    

def aplicar_descuento(precios, porcentaje):
    """
    TODO: Implementa una función que use comprensión de diccionarios para crear
    un nuevo diccionario con los precios con descuento
    Ejemplo: para 20% -> {"manzana": 712, "pera": 600, ...}
    """
    descuento = {}
    for fruta, precio in precios.items():   #sirve para que pueda recuperar tanto el valor como el nombre de forma independiente
        descuento_precio = precio * (porcentaje / 100)
        precio_final = precio - descuento_precio
        descuento[fruta] = precio_final
    return descuento

    return [precio -(precio * porcentaje / 100) for fruta,precio in precios.items()]


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
    assert aplicar_descuento(precios_test, 20) == {"a": 80, "b": 160}

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

#zip(lista1, lista2,)