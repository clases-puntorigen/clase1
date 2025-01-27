#!/usr/bin/env python3

"""
Ejercicio 1: Variables y Tipos de Datos

Este ejercicio te ayudará a entender:
- Cómo declarar variables
- Diferentes tipos de datos en Python
- Operaciones básicas con cadenas de texto
- Conversión de tipos
"""

# TODO: Crea una variable llamada 'name' y asígnale tu nombre
name ="jose"

# TODO: Crea una variable llamada 'age' y asígnale tu edad como número

age = 20

# TODO: Crea una variable llamada 'height' con tu altura en metros (usa un float)

height = 1.7

# TODO: Crea una variable booleana llamada 'is_student'

is_student = True

def main():
    # Esto generará un NameError si no has creado las variables
    print(f"Nombre: {name}")
    print(f"Edad: {age}")
    print(f"Altura: {height} metros")
    print(f"¿Es estudiante? {is_student}")
    
    # TODO: Intenta convertir tu edad a una cadena de texto y concatenarla con el texto "años"
    # Ejemplo de salida: "20 años"
    edad = "40"
    pablo_tiene = int(edad) + 5 
    age_string = str(age) + " años"  # Tu código aquí
    print(age_string)
    
    # TODO: Calcula tu edad en días (aproximadamente)
    # Pista: multiplica tu edad por 365
    age_in_days = age * 365  # Tu código aquí
    print(f"Tienes aproximadamente {age_in_days} días de edad")

if __name__ == "__main__":
    main()
