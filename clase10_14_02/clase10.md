# Clases en Python: Una Guía Completa

En esta guía, exploraremos en detalle las clases en Python, sus componentes y cómo podemos trabajar con ellas de manera dinámica.

## Índice
1. [Estructura Básica de una Clase](#estructura-básica-de-una-clase)
2. [Docstrings](#docstrings)
3. [Atributos y Propiedades](#atributos-y-propiedades)
4. [Métodos](#métodos)
5. [Clases con Pydantic](#clases-con-pydantic)
6. [Reflexión y Metaprogramación](#reflexión-y-metaprogramación)

## Estructura Básica de una Clase

Una clase en Python es una plantilla para crear objetos. Aquí un ejemplo básico:

```python
class Persona:
    """
    Esta es una clase que representa a una persona.
    """
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
```
    
## Docstrings

Los docstrings son cadenas de documentación que describen el propósito y funcionamiento de una clase o método:

```python
class Calculadora:
    """
    Clase que implementa operaciones matemáticas básicas.
    
    Attributes:
        ultimo_resultado (float): Almacena el último resultado calculado
    
    Example:
        >>> calc = Calculadora()
        >>> calc.sumar(5, 3)
        8
    """
    
    def sumar(self, a: float, b: float) -> float:
        """
        Suma dos números.
        
        Args:
            a (float): Primer número
            b (float): Segundo número
            
        Returns:
            float: La suma de los dos números
        """
        self.ultimo_resultado = a + b
        return self.ultimo_resultado
```

## Atributos y Propiedades

Los atributos pueden definirse de varias formas:

```python
class Empleado:
    # Atributo de clase (compartido entre todas las instancias)
    empresa = "TechCorp"
    
    def __init__(self, nombre: str):
        # Atributo de instancia
        self._nombre = nombre
    
    # Propiedad con getter
    @property
    def nombre(self) -> str:
        return self._nombre
    
    # Propiedad con setter
    @nombre.setter
    def nombre(self, valor: str):
        if not valor:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor
```

## Métodos

Las clases pueden tener diferentes tipos de métodos:

```python
class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
    
    # Método de instancia
    def aplicar_descuento(self, porcentaje: float) -> float:
        return self.precio * (1 - porcentaje / 100)
    
    # Método de clase
    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(datos['nombre'], datos['precio'])
    
    # Método estático
    @staticmethod
    def validar_precio(precio: float) -> bool:    
        return precio > 0
```
    
## Clases con Pydantic

Pydantic es una biblioteca para validación de datos que utiliza anotaciones de tipo:

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Usuario(BaseModel):
    """
    Llena los campos para crear un usuario nuevo
    """
    id: int
    nombre: str
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    fecha_registro: datetime
    telefono: Optional[str] = None
    intereses: List[str] = []
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Ana García",
                "email": "ana@ejemplo.com",
                "fecha_registro": "2025-01-01T00:00:00",
                "intereses": ["python", "programación"]
            }
        }
    
# formulario
print("*** Llena los campos para crear un usuario nuevo ***")
nombre = input("dime tu nombre:")
email = input("dime tu email:")
telefono = input("dime tu telefono:")

jose = Usuario(nombre=nombre, email=email, telefono=telefono)

class PedirDatos:
    def __init__(self, clase):
        self.la_clase = clase
        self.nombre_de_la_clase_que_me_dieron = clase.__name__
        self.titulo = clase.__doc__
        print("** " + self.titulo + " **")
        respuestas = {}
        for nombre, valor in clase.__dict__.items():
            if isinstance(valor, property):
                pass
            elif callable(valor):
                pass
            else:
                respuestas[nombre] = input(f"Dime tu {nombre}")
        return clase(*respuestas)
    
    
jose = PedirDatos(Usuario)
# jose.nombre = "jose miguel"
# *** Llena los campos para crear un usuario nuevo ***
# dime tu nombre: _____ jose miguel
# dime tu email: _____
```

## Reflexión y Metaprogramación

Python permite inspeccionar y modificar clases y objetos en tiempo de ejecución:

```python
# Ejemplo de reflexión
def inspeccionar_clase(clase_o_instancia) -> dict:
    """
    Analiza una clase o instancia y retorna información sobre sus componentes.
    """
    # Obtener la clase si se pasó una instancia
    clase = clase_o_instancia if isinstance(clase_o_instancia, type) else type(clase_o_instancia)
    
    info = {
        "nombre": clase.__name__,
        "docstring": clase.__doc__,
        "atributos": {},
        "métodos": {},
        "propiedades": {}
    }
    
    # Inspeccionar atributos y métodos
    for nombre, valor in clase.__dict__.items():
        if isinstance(valor, property):
            info["propiedades"][nombre] = {
                "tipo": "propiedad",
                "doc": valor.__doc__
            }
        elif callable(valor):
            info["métodos"][nombre] = {
                "doc": valor.__doc__,
                "anotaciones": valor.__annotations__
            }
        else:
            info["atributos"][nombre] = {
                "valor": valor,
                "tipo": type(valor).__name__
            }
    
    return info

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear una instancia de Usuario
    usuario = Usuario(
        id=1,
        nombre="Ana García",
        email="ana@ejemplo.com",
        fecha_registro=datetime.now()
    )
    
    # Inspeccionar la clase
    info = inspeccionar_clase(usuario)
    
    # Acceder a atributos dinámicamente
    for nombre_attr in dir(usuario):
        if not nombre_attr.startswith('_'):  # Ignorar atributos privados
            valor = getattr(usuario, nombre_attr)
            print(f"{nombre_attr}: {valor}")
```

### Notas Importantes

1. Los docstrings son accesibles mediante el atributo `__doc__`
2. Las anotaciones de tipo se pueden acceder con `__annotations__`
3. Para clases Pydantic, se pueden usar métodos como:
   - `model_dump()`: Convertir a diccionario
   - `model_json()`: Convertir a JSON
   - `model_fields`: Acceder a la definición de campos

### Buenas Prácticas

1. Siempre incluir docstrings descriptivos
2. Usar anotaciones de tipo para mejor documentación
3. Mantener la responsabilidad única en las clases
4. Implementar propiedades para encapsulamiento cuando sea necesario
5. Utilizar validación de datos con Pydantic para datos externos

La reflexión es una herramienta poderosa, pero debe usarse con precaución ya que puede hacer el código más difícil de mantener si se abusa de ella.
