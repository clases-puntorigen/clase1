"""
Ejercicios de Pydantic

Completa los siguientes ejercicios para practicar el uso de Pydantic.
"""

from pydantic import BaseModel, ValidationError
from typing import List, Optional
from datetime import date

"""
Ejercicio 1: Sistema de Biblioteca
Crea un modelo para representar un libro y un sistema de préstamos.
- El libro debe tener: título, autor, año de publicación, ISBN (13 caracteres)
- Valida que el año no sea futuro
- El ISBN debe tener exactamente 13 caracteres
"""

# TODO: Implementa las clases Libro y Prestamo aquí


"""
Ejercicio 2: Sistema de Comercio Electrónico
Crea modelos para un sistema de comercio electrónico básico que incluya:
- Producto (nombre, precio, descripción, categoría, stock)
- Cliente (nombre, email, dirección de envío)
- Orden (cliente, productos, fecha, estado)

Requisitos:
- El precio debe ser positivo
- El stock debe ser >= 0
- El email debe ser válido
- La fecha no puede ser anterior a hoy
"""

# TODO: Implementa las clases Producto, Cliente y Orden aquí


"""
Ejercicio 3: Configuración de Aplicación
Crea un modelo para manejar la configuración de una aplicación web:
- Servidor: host, puerto, debug_mode
- Base de datos: url, usuario, contraseña, max_conexiones
- Cache: tipo_cache, tiempo_expiracion
- Logging: nivel, archivo_log

Requisitos:
- El puerto debe estar entre 1 y 65535
- max_conexiones debe ser positivo
- tiempo_expiracion en segundos (positivo)
- nivel de logging debe ser uno de: DEBUG, INFO, WARNING, ERROR, CRITICAL
"""

# TODO: Implementa la clase ConfiguracionApp aquí
