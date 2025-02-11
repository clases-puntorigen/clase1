"""
Ejercicio de Módulos Python - Importaciones y Exportaciones Básicas

En este ejercicio, aprenderás:
1. Cómo crear y usar módulos de Python
2. Cómo importar funciones desde otros archivos
3. Cómo usar las funciones importadas

Tareas:
1. Crea un nuevo archivo llamado 'calculadora.py' en el mismo directorio
2. En calculadora.py, define las siguientes funciones:
   - sumar(a, b): retorna la suma de a y b
   - restar(a, b): retorna a menos b
   - multiplicar(a, b): retorna a multiplicado por b
   - dividir(a, b): retorna a dividido por b (¡maneja la división por cero!)

3. Importa estas funciones en este archivo y úsalas para resolver los problemas siguientes
"""

# TODO: Importa las funciones requeridas desde calculadora.py
from calculadora import sumar, restar, multiplicar, division, nombreApp
from clase7_07_02.solutions.modules.calculadora import sumar, restar, multiplicar, division, nombreApp
from ejercicios.clases import MascotaVirtual

def principal():
    # Prueba tus funciones de calculadora aquí
    perro = MascotaVirtual()
    # 1. Calcula e imprime: 15 + 7
    print("15 + 7 = ", sumar(15,7))  # Debe usar la función sumar
    
    # 2. Calcula e imprime: 25 - 12
    print("25 - 12 = " , restar(25,12))  # Debe usar la función restar
    
    # 3. Calcula e imprime: 6 * 8
    print("6 * 8 = ", multiplicar(6,8))  # Debe usar la función multiplicar
    
    # 4. Calcula e imprime: 20 / 4
    print("20 / 4 = ", division(20,4))  # Debe usar la función dividir
    
    # 5. Prueba el manejo de división por cero
    print("10 / 0 = ", division(10,0))  # Debe manejar este caso adecuadamente
    

if __name__ == "__main__":
    principal()
