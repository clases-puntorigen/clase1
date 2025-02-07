#!/usr/bin/env python3

"""
Ejercicio: Introducción a Clases y Objetos en Python

Este ejercicio te ayudará a entender:
- Cómo crear clases y objetos
- Atributos y métodos de clase
- Constructor de clase (__init__)
- Métodos especiales (__str__)
- Encapsulamiento y validación de datos
"""

class MascotaVirtual:
    """
    TODO: Implementa la clase MascotaVirtual con los siguientes atributos:
    - nombre (str)
    - tipo (str) - ejemplo: "perro", "gato", "conejo"
    - energia (int) - valor entre 0 y 100
    - felicidad (int) - valor entre 0 y 100
    """
    
    def __init__(self, nombre: str, tipo: str):
        """
        TODO: Implementa el constructor de la clase
        Inicializa energia en 100 y felicidad en 50
        """
        self.nombre = nombre
        self.tipo = tipo
        self.energia = 100
        self.felicidad = 50

    def alimentar(self):
        """
        TODO: Implementa el método alimentar
        - Debe aumentar la energía en 20 puntos
        - La energía no puede superar 100
        """
        self.energia = min(100, self.energia+20)
        print(f"{self.nombre} ha comido")

    def jugar(self):
        """
        TODO: Implementa el método jugar
        - Debe aumentar la felicidad en 25 puntos
        - Debe reducir la energía en 15 puntos
        - Si no hay suficiente energía, mostrar mensaje de error
        - La felicidad no puede superar 100
        - La energía no puede ser menor que 0
        """
        if self.energia < 15:
            print(f"{self.nombre} no puede jugar, no tiene suficiente energia")
        else:
            self.felicidad = min(100, self.felicidad + 25)
            self.energia = max(0, self.energia - 15)
            print(f"Jugaste con {self.nombre}, su felicidad aumento a: {self.felicidad}, pero se canso un poco, su energia esta en: {self.energia}. ")

    def dormir(self):
        """
        TODO: Implementa el método dormir
        - Debe restaurar la energía a 100
        """
        self.energia = 100
        print(f"{self.nombre} ha dormido y su energia se recupero a: {self.energia}")
        
    def __str__(self):
        """
        TODO: Implementa el método especial __str__
        Debe retornar un string con el formato:
        "[nombre] ([tipo]) - Energía: [energia], Felicidad: [felicidad]"
        """
        return f"{self.nombre} ({self.tipo}) - Energia: {self.energia}, Felicidad: {self.felicidad}"

def test_mascota_virtual():
    # Test de creación de mascota
    mascota = MascotaVirtual("Luna", "gato")
    assert mascota.nombre == "Luna"
    assert mascota.tipo == "gato"
    assert mascota.energia == 100
    assert mascota.felicidad == 50

    # Test de alimentación
    mascota.energia = 50
    mascota.alimentar()
    assert mascota.energia == 70

    # Test de juego
    mascota.energia = 100
    mascota.felicidad = 50
    mascota.jugar()
    assert mascota.energia == 85
    assert mascota.felicidad == 75

    # Test de dormir
    mascota.energia = 30
    mascota.dormir()
    assert mascota.energia == 100

    # Test de límites
    mascota.energia = 90
    mascota.alimentar()
    assert mascota.energia == 100  # No debe superar 100

    mascota.felicidad = 90
    mascota.jugar()
    assert mascota.felicidad == 100  # No debe superar 100

def main():
    # Crear dos mascotas de prueba
    mascota1 = MascotaVirtual("Luna", "gato")
    mascota2 = MascotaVirtual("Rocky", "perro")

    print("=== Estado Inicial ===")
    print(mascota1)
    print(mascota2)

    # Interactuar con las mascotas
    print("\n=== Interactuando con las mascotas ===")
    mascota1.jugar()
    mascota1.alimentar()
    mascota2.jugar()
    mascota2.dormir()

    print("\n=== Estado Final ===")
    print(mascota1)
    print(mascota2)

    # Ejecutar pruebas
    test_mascota_virtual()
    print("\n¡Todas las pruebas pasaron exitosamente!")

if __name__ == "__main__":
    main()