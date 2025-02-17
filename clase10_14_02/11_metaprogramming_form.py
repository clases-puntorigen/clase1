
"""
Solución: Generador de Formularios con Pydantic
"""
from pydantic import BaseModel, Field
from typing import Optional, Any, get_args, get_origin, Union
from datetime import date
import json
from datetime import datetime

def obtener_valor_campo(campo: str, tipo: Any, info: Field) -> Any:
    """
    Solicita y valida un valor para un campo específico.
    """
    descripcion = info.description or campo
    es_opcional = info.default is None and not info.is_required()
    
    """
    En Python moderno, los tipos genéricos como Optional[T] son en realidad tipos compuestos.
    Por ejemplo, Optional[date] es internamente Union[date, None].
    
    Para extraer el tipo real necesitamos:
    1. get_origin(tipo): Obtiene el tipo base de un tipo genérico.
       - Para Optional[date] retorna Union
       - Para List[int] retorna list
       - Para un tipo simple como str retorna None
    
    2. get_args(tipo): Obtiene los argumentos de tipo del tipo genérico.
       - Para Optional[date] retorna (date, NoneType)
       - Para List[int] retorna (int,)
       - Para Dict[str, int] retorna (str, int)
    
    Este bloque detecta si el tipo es Optional[T] verificando si:
    a) Es un Union (get_origin)
    b) Tiene exactamente 2 argumentos donde el segundo es NoneType (get_args)
    Si ambas condiciones se cumplen, extraemos el primer tipo que es el tipo real.
    """
    # Extraer el tipo real si es Optional
    tipo_real = tipo
    if get_origin(tipo) is Union:
        args = get_args(tipo)
        if len(args) == 2 and args[1] is type(None):  # Optional[T] es Union[T, None]
            tipo_real = args[0]
    
    while True:
        sufijo = " (opcional, presiona Enter para omitir)" if es_opcional else ""
        valor = input(f"{descripcion} ({tipo_real.__name__}){sufijo}: ").strip()
        
        # Manejar campo opcional vacío
        if es_opcional and not valor:
            return None
            
        try:
            # Manejar tipos especiales
            if tipo_real is date:
                if valor.lower() in ['hoy', 'today']:
                    return date.today()
                # Formato YYYY-MM-DD
                año, mes, dia = map(int, valor.split('-'))
                return date(año, mes, dia)
            elif tipo_real is bool:
                valor = valor.lower()
                if valor in ('true', 't', '1', 'si', 'sí', 'y', 'yes'):
                    return True
                elif valor in ('false', 'f', '0', 'no', 'n'):
                    return False
                raise ValueError()
            
            # Para otros tipos, dejar que Pydantic haga la validación
            return valor
            
        except (ValueError, TypeError):
            print(f"Error: Por favor ingresa un valor válido de tipo {tipo_real.__name__}")
            if tipo_real is date:
                print("Usa el formato YYYY-MM-DD o escribe 'hoy'")

def crear_modelo_desde_terminal(modelo: type[BaseModel]) -> BaseModel:
    """
    Crea una instancia del modelo Pydantic pidiendo los datos por terminal.
    
    Args:
        modelo: Clase del modelo Pydantic a instanciar
        
    Returns:
        Una instancia del modelo con los datos ingresados
    """
    # Mostrar información del modelo
    print(f"\n{'='*50}")
    print(f"Creando nuevo {modelo.__name__}")
    if modelo.__doc__:  #es una cadena de texto que contiene la documentación de la clase modelo.
        print(f"\nDescripción:")
        print(modelo.__doc__.strip())
    print(f"{'='*50}\n")
    
    # Recolectar valores para cada campo
    datos = {}
    for nombre, campo in modelo.model_fields.items():
        tipo = campo.annotation   #se utiliza para especificar que tipo de dato se espera para una variable
        if tipo is None:
            tipo = str  # tipo por defecto si no se especifica
            
        try:
            valor = obtener_valor_campo(nombre, tipo, campo)
            if valor is not None:  # solo incluir valores no-None
                datos[nombre] = valor
        except KeyboardInterrupt:
            print("\nOperación cancelada")
            return None
    
    # Crear y validar la instancia
    try:
        return modelo(**datos)
    except Exception as e:
        print(f"\nError al crear el modelo: {e}")
        return None

# Modelos de ejemplo
class Producto(BaseModel):
    """
    Modelo que representa un producto en el inventario.
    """
    nombre: str = Field(..., description="Nombre del producto")
    precio: float = Field(..., gt=0, description="Precio en pesos")
    stock: int = Field(..., ge=0, description="Cantidad disponible")
    disponible: bool = Field(True, description="¿Está disponible para la venta?")
    fecha_vencimiento: Optional[date] = Field(None, description="Fecha de vencimiento del producto")

class Empleado(BaseModel):
    """
    Modelo que representa a un empleado.
    """
    nombre: str = Field(..., min_length=2, description="Nombre completo")
    edad: int = Field(..., gt=18, lt=100, description="Edad del empleado")
    salario: float = Field(..., gt=0, description="Salario mensual")
    fecha_ingreso: date = Field(..., description="Fecha de ingreso a la empresa")
    activo: bool = Field(True, description="¿El empleado está activo?")

if __name__ == "__main__":
    # Probar con diferentes modelos
    print("Creando un producto:")
    producto = crear_modelo_desde_terminal(Producto)
    if producto:
        print("\nProducto creado:")
        print(producto.model_dump_json(indent=2))
    
    print("\nCreando un empleado:")
    empleado = crear_modelo_desde_terminal(Empleado)
    if empleado:
        print("\nEmpleado creado:")
        print(empleado.model_dump_json(indent=2))
