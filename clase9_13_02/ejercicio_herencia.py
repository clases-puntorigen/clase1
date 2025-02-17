"""
Ejercicios de Herencia en Python

Completa los siguientes ejercicios para practicar los conceptos de herencia.
"""

"""
Ejercicio 1: Sistema de Formas Geométricas

Crea un sistema de clases para manejar diferentes formas geométricas:
1. Crea una clase base abstracta 'Forma' con métodos abstractos 'area' y 'perimetro'
2. Implementa las clases 'Rectangulo', 'Circulo' y 'Triangulo' que hereden de 'Forma'
3. Cada clase debe implementar correctamente los métodos 'area' y 'perimetro'
4. Agrega un método 'descripcion' que retorne una descripción de la forma
"""
class Forma:
   def __init__(self,nombre):
      self.nombre = nombre
   def area(self):
      pass
   def perimetro(self):
      pass

   def descripcion(self):
      return f"forma geométrica llamada {self.nombre}"
   
class Rectangulo(Forma):
   def __init__(self,nombre, altura,ancho):
      super().__init__(nombre)
      self.altura = altura
      self.ancho = ancho
   
   def area(self):
      return self.altura * self.ancho

   def perimetro(self):
      return (self.altura + self.ancho) * 2

class Circulo(Forma):
   def __init__(self, nombre, radio):
      super().__init__(nombre)
      self.radio = radio

   def area(self):
      return 3.14159 * self.radio ** 2

   def perimetro(self):
      return 2 * 3.14159 * self.radio

class Triangulo(Forma):
   def __init__(self,nombre,base,altura,lado_a,lado_b,lado_c):
      super().__init__(nombre)
      self.base = base
      self.altura = altura
      self.lado_a = lado_a
      self.lado_b = lado_b
      self.lado_c = lado_c
   
   def area(self):
      return (self.base * self.altura) / 2

   def perimetro(self):
      return self.lado_a + self.lado_b + self.lado_c

"""
Ejercicio 2: Sistema de Empleados

Crea un sistema de gestión de empleados con las siguientes características:
1. Clase base 'Empleado' con atributos: nombre, id, salario_base
2. Subclases: 'Gerente', 'Vendedor', 'Desarrollador'
3. Cada tipo de empleado debe tener:
   - Un método para calcular su salario total (incluyendo bonos)
   - Un método para generar su descripción de cargo
   - Atributos específicos según su rol
"""

class Empleado:
   def __init__(self,nombre,id,salario_base):
      self.nombre = nombre
      self.id = id
      self.salario_base = salario_base

   def calcular_pago(self):
      return self.salario_base

class Gerente(Empleado):
   def __init__(self, nombre, id, salario_base, bono):
      super().__init__(nombre,id,salario_base)
      self.bono = bono

   def calcular_pago(self):
      return self.salario_base + self.bono
   
   def descripcion(self):
      return f"Empleado: {self.nombre}, ID: {self.id}"

class Vendedor(Empleado):
   def __init__(self, nombre, id, salario_base, comision):
      super().__init__(nombre,id,salario_base)
      self.comision = comision

   def calcular_pago(self):
      return self.salario_base + self.comision
   
   def descripcion(self):
      return f"Vendedor: {self.nombre}, comision: {self.comision}"
   
class Desarrollador(Empleado):
   def __init__(self, nombre, id, salario_base,horas_extra):
      super().__init__(nombre, id, salario_base)
      self.horas_extra = horas_extra

   def calcular_pago(self):
      return self.salario_base + self.horas_extra

   def descripcion(self):
      return f"Desarrollador: {self.nombre}, Horas extra: {self.horas_extra}"  


"""
Ejercicio 3: Sistema de Vehículos

Implementa un sistema de vehículos utilizando herencia múltiple:
1. Crea las clases base: 'Vehiculo', 'VehiculoElectrico', 'VehiculoDeportivo'
2. Implementa la clase 'TeslaModelS' que herede de 'Vehiculo' y 'VehiculoElectrico'
3. Implementa la clase 'PorscheTaycan' que herede de todas las clases base
4. Incluye métodos para:
   - Calcular autonomía
   - Mostrar características
   - Calcular aceleración
"""

# TODO: Implementa las clases aquí


"""
Ejercicio 4: Sistema de Cuentas Bancarias

Diseña un sistema de cuentas bancarias con las siguientes especificaciones:
1. Clase base 'CuentaBancaria' con:
   - Métodos para depositar y retirar dinero
   - Propiedad para consultar saldo
   - Método para generar estado de cuenta
2. Implementa las subclases:
   - 'CuentaAhorro': con tasa de interés y cálculo de intereses
   - 'CuentaCorriente': con límite de sobregiro
   - 'CuentaInversion': con tipos de inversiones y cálculo de rendimientos
"""

# TODO: Implementa las clases aquí


if __name__ == "__main__":
    # Puedes agregar código de prueba aquí
    pass
