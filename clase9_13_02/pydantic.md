# Tutorial de Pydantic

## ¿Qué es Pydantic?

Pydantic es una biblioteca de Python que proporciona validación de datos mediante anotaciones de tipo. Es especialmente útil para:
- Validar datos de entrada
- Serializar y deserializar datos
- Gestionar configuraciones
- Garantizar la integridad de los datos en tiempo de ejecución

## Instalación

```bash
pip install pydantic
```

## Conceptos Básicos

### 1. Modelos Básicos

Los modelos son la base de Pydantic. Se crean heredando de `BaseModel`:

```python
from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    nombre: str
    edad: int
    email: str
    activo: bool = True  # Campo con valor por defecto
    biografia: Optional[str] = None  # Campo opcional
```

### 2. Tipos de Datos Básicos

Pydantic soporta varios tipos de datos nativos de Python:

```python
from datetime import datetime, date
from typing import List, Dict

class Evento(BaseModel):
    id: int
    nombre: str
    fecha: date
    hora: datetime
    etiquetas: List[str]
    metadatos: Dict[str, str]
```

### 3. Validación de Campos

#### 3.1 Usando Field

`Field` permite definir restricciones y metadatos para los campos:

```python
from pydantic import BaseModel, Field

class Producto(BaseModel):
    nombre: str = Field(..., min_length=3)
    precio: float = Field(..., gt=0)
    descripcion: str = Field(
        default="Sin descripción",
        max_length=1000
    )
    stock: int = Field(..., ge=0)
```

Restricciones comunes:
- `gt`, `ge`: mayor que, mayor o igual que
- `lt`, `le`: menor que, menor o igual que
- `min_length`, `max_length`: longitud mínima/máxima para strings
- `regex`: expresión regular para validar strings

### 4. Validadores Personalizados

#### 4.1 Validadores de Campo (@field_validator)

```python
from pydantic import BaseModel, field_validator
from datetime import date

class Reserva(BaseModel):
    fecha_inicio: date
    fecha_fin: date

    @field_validator('fecha_fin')
    def validar_fechas(cls, valor, info):
        fecha_inicio = info.data.get('fecha_inicio')
        if fecha_inicio and valor < fecha_inicio:
            raise ValueError('La fecha de fin no puede ser anterior a la fecha de inicio')
        return v
```

#### 4.2 Validadores de Modelo (@model_validator)

```python
from pydantic import BaseModel, model_validator

class Descuento(BaseModel):
    porcentaje: float
    monto_maximo: float

    @model_validator(mode='after')
    def validar_descuento(self):
        if self.porcentaje < 0 or self.porcentaje > 100:
            raise ValueError('El porcentaje debe estar entre 0 y 100')
        if self.monto_maximo < 0:
            raise ValueError('El monto máximo no puede ser negativo')
        return self
```

### 5. Modelos Anidados

Pydantic permite anidar modelos dentro de otros modelos:

```python
class Direccion(BaseModel):
    calle: str
    ciudad: str
    codigo_postal: str
    pais: str = "Chile"

class Cliente(BaseModel):
    nombre: str
    direcciones: List[Direccion]
    direccion_principal: Direccion

```

### 6. Enumeraciones

```python
from enum import Enum

class EstadoPedido(str, Enum):
    PENDIENTE = "pendiente"
    CONFIRMADO = "confirmado"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"

class Pedido(BaseModel):
    id: int
    estado: EstadoPedido = EstadoPedido.PENDIENTE
```

### 7. Métodos Útiles de los Modelos

#### 7.1 Serialización

```python
usuario = Usuario(nombre="Ana", edad=25, email="ana@ejemplo.com")

# Convertir a diccionario
dict_usuario = usuario.model_dump()

# Convertir a JSON
json_usuario = usuario.model_dump_json()

# Excluir campos
dict_sin_email = usuario.model_dump(exclude={'email'})

# Incluir solo ciertos campos
dict_basico = usuario.model_dump(include={'nombre', 'edad'})
```

#### 7.2 Actualización de Modelos

```python
usuario = Usuario(nombre="Ana", edad=25, email="ana@ejemplo.com")
usuario_actualizado = usuario.model_copy(update={"edad": 26})
```

### 8. Buenas Prácticas

1. **Tipos Explícitos**: Siempre especifica los tipos de datos de forma explícita.
```python
# Bien
edad: int
# Mal
edad = None
```

2. **Valores por Defecto**: Usa `Optional` para campos que pueden ser None.
```python
# Bien
descripcion: Optional[str] = None
# Mal
descripcion: str = None
```

3. **Validación Temprana**: Valida los datos lo antes posible.
```python
# Bien
@field_validator('edad')
def validar_edad(cls, v):
    if v < 0:
        raise ValueError('La edad no puede ser negativa')
    return v
```

4. **Documentación**: Usa docstrings y comentarios para explicar la lógica compleja.
```python
class Usuario(BaseModel):
    """
    Modelo que representa un usuario en el sistema.
    
    Attributes:
        nombre: Nombre completo del usuario
        edad: Edad en años (debe ser positiva)
        email: Dirección de correo electrónico válida
    """
    nombre: str
    edad: int
    email: str
```

### 9. Manejo de Errores

```python
from pydantic import ValidationError

try:
    usuario = Usuario(
        nombre="Ana",
        edad="no es un número",  # Esto causará un error
        email="correo_invalido"
    )
except ValidationError as e:
    print(e.errors())  # Lista detallada de errores
    print(e.json())    # Errores en formato JSON
```

## Conclusión

Pydantic es una herramienta poderosa para la validación de datos en Python. Sus principales ventajas son:
- Sintaxis clara y declarativa
- Validación automática de tipos
- Excelente integración con type hints de Python
- Alto rendimiento
- Buena documentación y soporte de la comunidad

## Recursos Adicionales

- [Documentación oficial de Pydantic](https://docs.pydantic.dev/)
- [Guía de migración a Pydantic V2](https://docs.pydantic.dev/latest/migration/)
