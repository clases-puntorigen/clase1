"""
Ejercicio: Creación y Uso de Administradores de Contexto

En este ejercicio, crearemos varios administradores de contexto útiles
y los usaremos para resolver problemas prácticos.

Tareas:
1. Implementar un administrador de contexto para medir tiempo
2. Crear un administrador para manejar archivos temporales
3. Desarrollar un sistema de logging contextual
"""

import os
import time
from contextlib import contextmanager
from typing import Optional


# TODO: Implementar el administrador de contexto TemporizadorContexto
# Debe medir el tiempo transcurrido y mostrar un mensaje al finalizar
class TemporizadorContexto:
    def __init__(self, descripcion: str):
        self.descripcion = descripcion
    
    def __enter__(self):
        self.inicio = time()
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        fin = time()
        duracion = fin - self.inicio
        print(f"La duracion fue de:{duracion:..2f}segundos")



# TODO: Implementar el administrador de contexto para archivos temporales
# Debe crear un archivo temporal y eliminarlo al finalizar
@contextmanager
def archivo_temporal(contenido: str = "") -> str:
    
    try:
        with open ('entrada.txt','r') as archivo:
            nombre = archivo.read()
        yield nombre
    finally:
        if os.path.exists(nombre):
            os.remove(nombre)

    """
# TODO: Implementar el administrador de contexto para logging
class RegistroContextual:
    """
   # Administrador de contexto que registra eventos con nivel de anidamiento
    """
    Ejemplo de uso:
    with RegistroContextual("Tarea Principal"):
        print("Haciendo tarea principal")
        with RegistroContextual("Subtarea"):
            print("Haciendo subtarea")
    
    Salida esperada:
    [Tarea Principal] Iniciando...
        Haciendo tarea principal
        [Subtarea] Iniciando...
            Haciendo subtarea
        [Subtarea] Completado
    [Tarea Principal] Completado
    """
    _nivel = 0  # Variable de clase para tracking del nivel de anidamiento
    
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_value, traceback):
        pass

def probar_temporizador():
    """Prueba el administrador de contexto TemporizadorContexto"""
    print("\n1. Probando TemporizadorContexto:")
    with TemporizadorContexto("Operación costosa"):
        # Simular operación que toma tiempo
        time.sleep(0.5)


def probar_archivo_temporal():
    """Prueba el administrador de contexto archivo_temporal"""
    print("\n2. Probando archivo_temporal:")
    with archivo_temporal("Contenido de prueba") as ruta:
        print(f"Archivo temporal creado en: {ruta}")
        with open(ruta, 'r') as f:
            contenido = f.read()
            print(f"Contenido: {contenido}")
    print("¿Archivo existe?:", os.path.exists(ruta))


def probar_registro():
# Prueba el administrador de contexto RegistroContextual
    print("\n3. Probando RegistroContextual:")
    with RegistroContextual("Proceso Principal"):
        print("Iniciando proceso principal")
        with RegistroContextual("Subproceso 1"):
            print("Ejecutando subproceso 1")
        with RegistroContextual("Subproceso 2"):
            print("Ejecutando subproceso 2")
            with RegistroContextual("Tarea"):
                print("Ejecutando tarea")


def main():
    print("🧪 Probando administradores de contexto...")
    probar_temporizador()
    probar_archivo_temporal()
    probar_registro()
    print("\n✨ Pruebas completadas!")


if __name__ == "__main__":
    main()
