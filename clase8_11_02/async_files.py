"""
Ejercicio: Sistema de Procesamiento de Archivos de Registro

En este ejercicio, crearemos un sistema que procese múltiples archivos de registro
simultáneamente usando operaciones asíncronas.

Tareas:
1. Implementar funciones para leer y escribir archivos de manera asíncrona
2. Procesar múltiples archivos de registro en paralelo
3. Agregar marcas de tiempo y estadísticas al procesamiento
"""

import asyncio
import aiofiles
from datetime import datetime
from pathlib import Path

# TODO: Implementar función para procesar una línea de registro
# La función debe:
# - Agregar marca de tiempo al inicio de la línea
# - Convertir la línea a mayúsculas
# - Contar el número de palabras
async def procesar_linea(linea: str) -> tuple[str, int]:
    pass

# TODO: Implementar función para procesar un archivo completo
# La función debe:
# - Leer el archivo de entrada línea por línea usando aiofiles.open()
# - Procesar cada línea usando procesar_linea()
# - Escribir las líneas procesadas en un nuevo archivo
# - Asegurarse de cerrar los archivos correctamente usando try/finally
# - Retornar el total de palabras procesadas
async def procesar_archivo(archivo_entrada: Path) -> int:
    total_palabras = 0
    archivo_salida = archivo_entrada.with_suffix('.procesado.txt')
    
    entrada = None
    salida = None
    try:
        # TODO: Implementar la lógica de procesamiento aquí
        pass
    finally:
        # TODO: Cerrar los archivos si están abiertos
        pass
    
    return total_palabras

# TODO: Implementar función para procesar múltiples archivos
# La función debe:
# - Crear una tarea para cada archivo usando asyncio.create_task()
# - Procesar todos los archivos en paralelo usando asyncio.gather()
# - Retornar una lista con el total de palabras por archivo
async def procesar_archivos(archivos: list[Path]) -> list[int]:
    pass

async def main():
    # Archivos de ejemplo (serán creados automáticamente)
    archivos = [
        Path("registro1.txt"),
        Path("registro2.txt"),
        Path("registro3.txt")
    ]
    
    # Crear archivos de ejemplo si no existen
    for i, archivo in enumerate(archivos, 1):
        archivo_temp = None
        try:
            archivo_temp = open(archivo, 'w')
            archivo_temp.write(f"línea 1 del registro {i}\n")
            archivo_temp.write(f"esta es la línea 2 del archivo {i}\n")
            archivo_temp.write(f"última línea del registro {i}\n")
        finally:
            if archivo_temp:
                archivo_temp.close()
    
    print(" Iniciando procesamiento de archivos...")
    inicio = datetime.now()
    
    # TODO: Procesar todos los archivos y obtener estadísticas
    palabras_por_archivo = await procesar_archivos(archivos)
    
    tiempo = datetime.now() - inicio
    print(f" Procesamiento completado en {tiempo.total_seconds():.2f} segundos")
    
    # TODO: Mostrar estadísticas de procesamiento
    # - Total de archivos procesados
    # - Total de palabras por archivo
    # - Total global de palabras

if __name__ == "__main__":
    asyncio.run(main())
