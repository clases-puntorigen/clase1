#!/usr/bin/env python3

"""
Ejercicio 5: Manipulación Simple de Textos en Python

Este ejercicio te ayudará a entender:
- Cómo crear y modificar textos
- Cómo convertir entre mayúsculas y minúsculas
- Cómo juntar textos
- Cómo buscar dentro de un texto
"""

def convertir_nombre(nombre):
    """
    TODO: Convierte un nombre para que tenga la primera letra mayúscula
    y el resto en minúsculas.
    
    Por ejemplo:
    convertir_nombre("JUAN") -> "Juan"
    convertir_nombre("maría") -> "María"
    
    PISTA: Usa los métodos .lower() y .capitalize()
    """

    nombre_convertido = nombre.lower().capitalize()
    return nombre_convertido

def crear_saludo(nombre):
    """
    TODO: Crea un saludo que diga "¡Hola, [nombre]!"
    
    Por ejemplo:
    crear_saludo("Ana") -> "¡Hola, Ana!"
    crear_saludo("Pedro") -> "¡Hola, Pedro!"
    
    PISTA: Usa + o f-strings para juntar textos
    """
    saludo_creado = f"!Hola {nombre}¡"
    return saludo_creado

def contar_letra(texto, letra):
    """
    TODO: Cuenta cuántas veces aparece una letra en un texto.
    No debe importar si la letra está en mayúsculas o minúsculas.
    
    Por ejemplo:
    contar_letra("Programacion", "a") -> 2
    contar_letra("Python", "y") -> 1
    
    PISTA: Convierte todo a minúsculas con .lower() y usa .count()

    """
    # Aqui intente de varias formas, y que me resulto fue la siguiente:

    minusculas = texto.lower() 
    minusculas2 = letra.lower()
    contador_texto = minusculas.count("a")
    return contador_texto

    #minusculas = texto.lower() and letra.lower()
    #contador_texto = minusculas.count("a")
    #return contador_texto

def es_pregunta(texto):
    """
    TODO: Revisa si un texto termina con signo de interrogación.
    
    Por ejemplo:
    es_pregunta("¿Cómo estás?") -> True
    es_pregunta("Hola") -> False
    
    PISTA: Usa el método .endswith() para revisar el final del texto
    """

    es_una_pregunta = texto.endswith("?")
    return es_una_pregunta

    

def main():
    # Prueba 1: Convertir nombres
    print("=== Convirtiendo Nombres ===")
    nombres = ["JUAN", "maría", "PeDrO", "ANA"]
    for nombre in nombres:
        convertido = convertir_nombre(nombre)
        print(f"{nombre} -> {convertido}")
    
    # Prueba 2: Crear saludos
    print("\n=== Creando Saludos ===")
    nombres = ["Ana", "Pedro", "María"]
    for nombre in nombres:
        saludo = crear_saludo(nombre)
        print(saludo)
    
    # Prueba 3: Contar letras
    print("\n=== Contando Letras ===")
    print("'a' en 'Programacion':", contar_letra("Programacion", "a"))
    print("'y' en 'Python':", contar_letra("Python", "y"))
    print("'e' en 'Desarrollo':", contar_letra("Desarrollo", "e"))
    
    # Prueba 4: Revisar preguntas
    print("\n=== Revisando Preguntas ===")
    frases = [
        "¿Cómo estás?",
        "Hola",
        "¿Qué hora es?",
        "Adiós"
    ]
    for frase in frases:
        if es_pregunta(frase):
            print(f"'{frase}' es una pregunta")
        else:
            print(f"'{frase}' no es una pregunta")

if __name__ == "__main__":
    main()
