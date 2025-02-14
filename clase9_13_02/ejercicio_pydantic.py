"""
Ejercicios de Pydantic

Completa los siguientes ejercicios para practicar el uso de Pydantic.
"""

from pydantic import BaseModel, ValidationError,field_validator,Field
from typing import List, Optional
from datetime import date
from enum import Enum
"""
Ejercicio 1: Sistema de Biblioteca
Crea un modelo para representar un libro y un sistema de préstamos.
- El libro debe tener: título, autor, año de publicación, ISBN (13 caracteres)
- Valida que el año no sea futuro
- El ISBN debe tener exactamente 13 caracteres
"""
class Libro(BaseModel):
    titulo: str
    autor: str
    anio_de_publicacion: int
    ISBN: str = Field(...,min_length=13,max_length=13)

    @field_validator('anio_de_publicacion')
    def validacion_anio(cls,v,info):
        if v > date.today().year:
            raise ValueError('El año de publicacion es una fecha que aun no ah pasado')
    
    
    """
    esta malo fue parte del proceso 
    @field_validator('año_de_publicacion')
    def validacion_año(cls,v,info):
        fecha_inicio = info.data.get
        ('fecha_incio')
        if fecha_inicio and año_de_publicacion < fecha_inicio:
            raise ValueError('')
    """

"""
Ejercicio 2: Sistema de Comercio Electrónico
Crea modelos para un sistema de comercio electrónico básico que incluya:
- Producto (nombre, precio, descripción, categoría, stock)
- Cliente (nombre, email, dirección de envío)
- Orden (cliente, productos, fecha, estado)

Requisitos:
- El precio debe ser positivo *
- El stock debe ser >= 0 *
- El email debe ser válido
- La fecha no puede ser anterior a hoy
"""

class Producto(BaseModel):
    nombre: str
    precio: float = Field(..., gt=0) #esto hace que debe ser mayor a 0
    descripción: str
    categoria: str
    stock: int = Field(...,ge=0)  #esto permite que sea igual a 0

class Cliente(BaseModel):
    nombre: str
    email: str = Field(...,pattern=r"^\S+@\S+\.\S+$")
    direccion_envio: str

class Orden(BaseModel):
    cliente: str
    productos: str
    fecha: date
    estado: str

jose = Cliente(nombre = "jose",email ="ola@gmail.com",direccion_envio = "los pescadores")
print(jose)
"""
Ejercicio 3: Configuración de Aplicación
Crea un modelo para manejar la configuración de una aplicación web:
- Servidor: host, puerto, debug_mode
- Base de datos: url, usuario, contraseña, max_conexiones
- Cache: tipo_cache, tiempo_expiracion
- Logging: nivel, archivo_log

Requisitos:
- El puerto debe estar entre 1 y 65535*
- max_conexiones debe ser positivo*
- tiempo_expiracion en segundos (positivo)*
- nivel de logging debe ser uno de: DEBUG, INFO, WARNING, ERROR, CRITICAL*
"""

class Servidor(BaseModel):
    host: str
    puerto: int = Field(..., ge=1,le= 65535)
    debug_mode: bool

class Basededatos(BaseModel):
    url: str
    usuario: str
    contrasena: str
    max_conexiones: int = Field(..., gt=0)

class Cache(BaseModel):
    tipo_cache: str
    tiempo_expiracion: int = Field(..., gt=0)

class Logging(str,Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


