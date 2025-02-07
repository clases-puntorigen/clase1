class CuentaBancaria:
    def __init__(self, titular: str, limite_retiro: float = 500):
        """
        TODO: Implementa el constructor de la cuenta bancaria.
        - Inicializa 'titular' con el nombre del titular.
        - 'saldo' debe empezar en 0.
        - 'limite_retiro' define la cantidad máxima que se puede retirar en una operación.
        """
        # PISTA: Usa 'self.atributo = valor' para definir los atributos.
        self.titular = titular
        self.saldo = 0
        self.limite_retiro = limite_retiro
    
    def depositar(self, cantidad: float):
        """
        TODO: Implementa el método depositar.
        - Aumenta el saldo en la cantidad depositada.
        """
        # PISTA: Usa 'self.saldo += cantidad' para actualizar el saldo.
        self.saldo += cantidad

    
    def retirar(self, cantidad: float):
        """
        TODO: Implementa el método retirar.
        - Verifica si hay suficiente saldo.
        - Verifica que la cantidad a retirar no supere 'limite_retiro'.
        - Si ambas condiciones se cumplen, resta la cantidad del saldo.
        - Si no, muestra un mensaje indicando el problema.
        """
        # PISTA: Usa 'if' para verificar las condiciones antes de restar del saldo.
        if cantidad > self.saldo:
            print(f"No puede retirar su salgo es: {self.saldo}")
        elif cantidad > self.limite_retiro:
            print(f"La cantidad máxima que puede retirar es {self.limite_retiro}.")
        else:
            self.saldo -= cantidad
            print(f"Se ha retirado {cantidad}. Nuevo saldo: {self.saldo}.")

    def consultar_saldo(self):
        """
        TODO: Implementa el método consultar_saldo.
        - Devuelve un string con el saldo actual.
        """
        # PISTA: Usa un f-string para formatear el saldo.
        print(f"Su saldo es: {self.saldo}")

def test_cuenta_bancaria():
    """
    Pruebas para la clase CuentaBancaria.
    """
    cuenta = CuentaBancaria("Jose", 1000)

    # Verificar el saldo inicial
    assert cuenta.saldo == 0
    assert cuenta.titular == "Jose"
    
    # Depositar dinero
    cuenta.depositar(500)
    assert cuenta.saldo == 500
    
    # Intentar retirar dentro del saldo y límite
    cuenta.retirar(200)
    assert cuenta.saldo == 300

    # Intentar retirar más del saldo
    cuenta.retirar(400)
    assert cuenta.saldo == 300  # No debe cambiar

    # Intentar retirar más del límite
    cuenta.retirar(1200)
    assert cuenta.saldo == 300  # No debe cambiar

    # Consultar saldo final
    cuenta.consultar_saldo()

def main():
    """
    Función principal para simular una cuenta bancaria.
    """
    # Crear cuenta bancaria
    cuenta1 = CuentaBancaria("Jose", 1000)
    cuenta1.consultar_saldo()  # Ver saldo inicial
    
    # Depositar dinero
    cuenta1.depositar(500)
    
    # Retirar dinero
    cuenta1.retirar(200)
    cuenta1.retirar(400)  # Intentar retirar más de lo que tiene
    cuenta1.retirar(1200)  # Intentar retirar más del límite
    
    # Consultar saldo final
    cuenta1.consultar_saldo()

if __name__ == "__main__":
    main()
    test_cuenta_bancaria()  # Ejecutar pruebas
