class Vehiculo:
    def __init__(self, marca: str, modelo: str):
        """
        Inicializa los atributos de la clase Vehiculo.

        - marca (str): Nombre de la marca del vehículo
        - modelo (str): Modelo del vehículo
        - combustible (int): Inicialmente en 100
        - kilometraje (int): Inicialmente en 0
        """
        self.marca = marca  
        self.modelo = modelo
        self.combustible = 100
        self.kilometraje = 0

    def conducir(self, km: int):
        """
        Reduce el combustible en 1 unidad por cada 10 km recorridos.
        Aumenta el kilometraje si hay suficiente combustible.
        # PISTA: Calcula cuánta gasolina se necesita con "km // 10"
        # PISTA: Usa 'if' para verificar si hay suficiente combustible antes de restarlo.
        """
        gasolina = km // 10
        if self.combustible >= gasolina:
            self.combustible -= gasolina
            self.kilometraje += km
            print(f"{self.modelo} ha recorrido {km}KM")
        else:
            print(f"{self.modelo} no tiene suficiente combustible")

    def recargar_combustible(self, cantidad: int):
        """
        Aumenta el nivel de combustible sin superar 100.
        # PISTA: Usa 'min(100, self.combustible + cantidad)' para evitar que supere 100.
        """
        self.combustible = min(100, self.combustible + cantidad)
        print(f"{self.modelo} tiene {self.combustible} de combustible")

    def estado(self):
        """
        Devuelve un string con el estado del vehículo.
        # PISTA: Usa f-strings para formatear la salida.
        """
        return f"{self.marca} - {self.modelo} - Combustible: {self.combustible}, Kilometraje: {self.kilometraje}"


def test_vehiculo():
    """
    Pruebas para la clase Vehiculo.
    """
    vehiculo = Vehiculo("Toyota", "Corolla")
    assert vehiculo.combustible == 100
    assert vehiculo.kilometraje == 0

    vehiculo.conducir(50)  # Debería gastar 5 de combustible
    assert vehiculo.combustible == 95
    assert vehiculo.kilometraje == 50

    vehiculo.recargar_combustible(10)
    assert vehiculo.combustible == 100  # No debe superar 100
    print("✅ Todas las pruebas pasaron correctamente.")


def main():
    """
    Simulación de vehículos.
    """
    vehiculo1 = Vehiculo("Toyota", "Corolla")
    vehiculo2 = Vehiculo("Ford", "Fiesta")

    print("=== Estado Inicial ===")
    print(vehiculo1.estado())
    print(vehiculo2.estado())

    print("\n=== Simulación de Viajes ===")
    vehiculo1.conducir(30)
    vehiculo2.conducir(50)

    print("\n=== Estado Final ===")
    vehiculo1.recargar_combustible(20)
    vehiculo2.recargar_combustible(30)

    print(vehiculo1.estado())
    print(vehiculo2.estado())


if __name__ == "__main__":
    main()
    test_vehiculo()
