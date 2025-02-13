# Tutorial de Herencia en Python

## ¿Qué es la Herencia?

La herencia es un concepto fundamental de la programación orientada a objetos que permite crear nuevas clases basadas en clases existentes. La nueva clase (subclase) hereda atributos y métodos de la clase base (superclase), permitiendo:
- Reutilización de código
- Extensión de funcionalidad
- Jerarquías de clases
- Polimorfismo

## Conceptos Básicos

### 1. Herencia Simple

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"
```

### 2. Constructor y super()

`super()` permite acceder a métodos de la clase padre:

```python
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
```

### 3. Métodos y Atributos

#### 3.1 Sobrescritura de Métodos

```python
class Figura:
    def calcular_area(self):
        return 0

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
```

#### 3.2 Extensión de Métodos

```python
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def calcular_pago(self):
        return self.salario

class Vendedor(Empleado):
    def __init__(self, nombre, salario, comision):
        super().__init__(nombre, salario)
        self.comision = comision
    
    def calcular_pago(self):
        return super().calcular_pago() + self.comision
```

### 4. Herencia Múltiple

Python permite heredar de múltiples clases:

```python
class DispositivoElectronico:
    def encender(self):
        return "Dispositivo encendido"

class Camara:
    def tomar_foto(self):
        return "Foto tomada"

class Telefono:
    def llamar(self):
        return "Llamando..."

class Smartphone(DispositivoElectronico, Camara, Telefono):
    pass
```

### 5. Métodos Especiales

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre} (${self.precio})"

class ProductoDescuento(Producto):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self.descuento = descuento
    
    def __str__(self):
        return f"{super().__str__()} - {self.descuento}% descuento"
```

### 6. Propiedades y Decoradores

```python
class Cuenta:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial
    
    @property
    def saldo(self):
        return self._saldo
    
    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            return True
        return False
    
    def retirar(self, monto):
        if monto > 0 and monto <= self._saldo:
            self._saldo -= monto
            return True
        return False

class CuentaAhorro(Cuenta):
    def __init__(self, saldo_inicial, tasa_interes):
        super().__init__(saldo_inicial)
        self.tasa_interes = tasa_interes
    
    @property
    def saldo_con_intereses(self):
        return self.saldo * (1 + self.tasa_interes)
    
    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes
        self.depositar(interes)
        return interes

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear una cuenta normal
    cuenta_basica = Cuenta(1000)
    print(f"Saldo inicial cuenta básica: ${cuenta_basica.saldo}")
    
    # Realizar operaciones en cuenta básica
    cuenta_basica.depositar(500)
    print(f"Saldo después de depósito: ${cuenta_basica.saldo}")
    
    cuenta_basica.retirar(200)
    print(f"Saldo después de retiro: ${cuenta_basica.saldo}")
    
    # Crear una cuenta de ahorro
    cuenta_ahorro = CuentaAhorro(2000, 0.05)  # 5% de interés
    print(f"\nSaldo inicial cuenta ahorro: ${cuenta_ahorro.saldo}")
    print(f"Saldo con intereses (proyección): ${cuenta_ahorro.saldo_con_intereses}")
    
    # Aplicar interés a la cuenta de ahorro
    interes_ganado = cuenta_ahorro.aplicar_interes()
    print(f"Interés ganado: ${interes_ganado}")
    print(f"Nuevo saldo después de aplicar interés: ${cuenta_ahorro.saldo}")
    
    # Demostrar que la cuenta de ahorro hereda métodos de Cuenta
    cuenta_ahorro.depositar(1000)
    print(f"Saldo después de depósito adicional: ${cuenta_ahorro.saldo}")
    print(f"Nuevo saldo con intereses (proyección): ${cuenta_ahorro.saldo_con_intereses}")

# Salida esperada:
# Saldo inicial cuenta básica: $1000
# Saldo después de depósito: $1500
# Saldo después de retiro: $1300
#
# Saldo inicial cuenta ahorro: $2000
# Saldo con intereses (proyección): $2100.0
# Interés ganado: $100.0
# Nuevo saldo después de aplicar interés: $2100.0
# Saldo después de depósito adicional: $3100.0
# Nuevo saldo con intereses (proyección): $3255.0
```

### 7. Clases Abstractas

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14159 * self.radio ** 2
    
    def perimetro(self):
        return 2 * 3.14159 * self.radio
```

## Buenas Prácticas

1. **Principio de Sustitución de Liskov**: Una subclase debe poder ser usada en lugar de su clase base sin alterar el comportamiento del programa.

2. **Composición sobre Herencia**: Cuando sea posible, prefiere la composición sobre la herencia.
```python
# Herencia
class AutoVolador(Auto):
    def volar(self):
        pass

# Composición (mejor)
class Auto:
    def __init__(self, motor):
        self.motor = motor

class Motor:
    def arrancar(self):
        pass
```

3. **Evitar Herencia Profunda**: No crear jerarquías de herencia demasiado profundas.

4. **Documentación Clara**: Documentar el propósito de la herencia y las responsabilidades de cada clase.

## Casos de Uso Comunes

1. **Jerarquías de Excepciones**:
```python
class MiError(Exception):
    pass

class ErrorDeValidacion(MiError):
    pass
```

2. **Plugins y Extensiones**:
```python
class Plugin:
    def ejecutar(self):
        pass

class PluginProcesamiento(Plugin):
    def ejecutar(self):
        return "Procesando datos..."
```

3. **Interfaces de Usuario**:
```python
class ComponenteBase:
    def renderizar(self):
        pass

class Boton(ComponenteBase):
    def renderizar(self):
        return "Renderizando botón"
```

4. **Modelos de Datos**:
```python
class ModeloBase:
    def guardar(self):
        pass
    
    def cargar(self):
        pass

class Usuario(ModeloBase):
    def __init__(self, nombre):
        self.nombre = nombre
```

## Conclusión

La herencia es una herramienta poderosa en la programación orientada a objetos, pero debe usarse con criterio. Es importante entender:
- Cuándo usar herencia vs composición
- Los principios SOLID
- Las limitaciones y ventajas de la herencia múltiple en Python
- La importancia de mantener jerarquías simples y claras
