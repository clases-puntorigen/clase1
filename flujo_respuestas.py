#!/usr/bin/env python3

"""
Ejercicio 2: Control de Flujo

Este ejercicio te ayudará a entender:
- Declaraciones if/elif/else
- Operadores de comparación
- Operadores lógicos
"""

def check_temperature(temp):
    """
    TODO: Escribe una función que retorne un mensaje basado en la temperatura:
    - Bajo 0: "¡Congelado!"
    - 0-15: "Frío"
    - 16-25: "Agradable"
    - Sobre 25: "¡Caluroso!"
    """
    if temp < 0:
        return "¡Congelado!"
    elif temp <= 15:
        return "Frío"
    elif temp <= 25:
        return "Agradable"
    else:
        return "¡Caluroso!"
    
    
def can_drive(age, has_license):
    """
    TODO: Escribe una función que determine si alguien puede conducir
    Deben cumplirse ambas condiciones:
    - Tener 18 años o más
    - Tener licencia
    Retorna True si puede conducir, False en caso contrario
    """
    #return age >= 18 and has_license
    if age >= 18 and has_license:
        return True
    else:
        return False

def main():
    # Prueba de la función de temperatura
    temperatures = [-5, 10, 20, 30]
    for temp in temperatures:
        message = check_temperature(temp)
        print(f"Cuando hace {temp}°C: {message}")
    
    # Prueba de la función de conducir
    test_cases = [
        (16, False),
        (20, True),
        (18, False),
        (25, True)
    ]
    
    for age, has_license in test_cases:
        can_they_drive = can_drive(age, has_license)
        print(f"Edad: {age}, Tiene licencia: {has_license} -> Puede conducir: {can_they_drive}")


if __name__ == "__main__":
    main()
