#!/usr/bin/env python3

"""
Ejercicio 9: Aprendiendo a usar input()

Este ejercicio te ayudará a entender:
- Cómo pedir información al usuario
- Cómo guardar lo que escribe el usuario
- Cómo convertir textos a números
- Cómo usar lo que el usuario escribe
"""

def saludar_usuario():
    """
    TODO: Pide el nombre al usuario y salúdalo.
    
    Ejemplo de cómo debería funcionar:
    > ¿Cómo te llamas? María
    > ¡Hola María! Bienvenida al programa.
    
    PISTA: Usa input() para preguntar y guardar la respuesta en una variable
    """
    nombre = input("¿Cómo te llamas? ").title()
    print(f"¡Hola {nombre}! Bienvenida al programa.")

def calcular_edad_en_meses():
    """
    TODO: Pide la edad al usuario y muestra cuántos meses tiene.
    
    Ejemplo de cómo debería funcionar:
    > ¿Cuántos años tienes? 5
    > ¡Tienes 60 meses de edad!
    
    PISTA 1: Recuerda que input() siempre devuelve texto
    PISTA 2: Usa int() para convertir el texto a número
    PISTA 3: Multiplica la edad por 12 para obtener los meses
    """
    edad = input("Ingrese su edad: ")
    meses = int(edad) * 12
    print(f"Tienes {meses} meses de edad")
    
def crear_tarjeta_presentacion():
    """
    TODO: Pide nombre y profesión al usuario, y crea una tarjeta de presentación.
    
    Ejemplo de cómo debería funcionar:
    > ¿Cuál es tu nombre? Juan Pérez
    > ¿Cuál es tu profesión? Profesor
    > +------------------------+
    > |     Juan Pérez        |
    > |      Profesor         |
    > +------------------------+
    
    PISTA 1: Usa input() dos veces para pedir los datos
    PISTA 2: Usa print() varias veces para mostrar la tarjeta
    """
    nombre = input("¿Cuál es tu nombre?")
    profesion = input("¿Cuál es tu profesión?")
    separador = "+------------------------+"
    print(separador)
    print(f"| {nombre.center(len(separador)-4)} |")
    print(f"| {profesion.center(len(separador)-4)} |")
    print(separador)

def calcular_precio_total():
    """
    TODO: Pide el precio de un producto y la cantidad deseada.
    Muestra el total a pagar.
    
    Ejemplo de cómo debería funcionar:
    > ¿Cuál es el precio del producto? 100
    > ¿Cuántas unidades quieres? 3
    > Total a pagar: $300
    
    PISTA 1: Usa float() para convertir el precio a número decimal
    PISTA 2: Usa int() para convertir la cantidad a número entero
    PISTA 3: Multiplica precio por cantidad
    """
    precio = float(input("¿Cuál es el precio del producto?"))
    unidades = int(input("¿Cuántas unidades quieres?"))
    total = precio * unidades
    print(f"El precio del producto es: {precio}, Y llevara {unidades} unidades, lo cual tiene un valor total de: {total}")

def main():
    print("=== Ejercicio 1: Saludos ===")
    saludar_usuario()
    
    print("\n=== Ejercicio 2: Edad en Meses ===")
    calcular_edad_en_meses()
    
    print("\n=== Ejercicio 3: Tarjeta de Presentación ===")
    crear_tarjeta_presentacion()
    
    print("\n=== Ejercicio 4: Calculadora de Precios ===")
    calcular_precio_total()

if __name__ == "__main__":
    main()
