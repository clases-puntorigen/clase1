# Tutorial: Operaciones Asíncronas con Archivos en Python

## Introducción

Cuando trabajamos con archivos, especialmente archivos grandes o muchos archivos a la vez, las operaciones de lectura y escritura pueden tomar tiempo. La programación asíncrona nos permite manejar estas operaciones de manera más eficiente.

## Operaciones con Archivos: Síncrono vs Asíncrono

### Enfoque Tradicional (Síncrono)
```python
# Lectura síncrona
archivo = open('archivo.txt', 'r')
contenido = archivo.read()
archivo.close()

# Escritura síncrona
archivo = open('salida.txt', 'w')
archivo.write('Hola Mundo')
archivo.close()
```

### Enfoque Moderno (Asíncrono)
```python
import asyncio
import aiofiles  # Necesitamos instalar: pip install aiofiles

async def leer_archivo():
    archivo = await aiofiles.open('archivo.txt', 'r')
    contenido = await archivo.read()
    await archivo.close()
    return contenido

async def escribir_archivo():
    archivo = await aiofiles.open('salida.txt', 'w')
    await archivo.write('Hola Mundo')
    await archivo.close()
```

## La Biblioteca aiofiles

`aiofiles` es una biblioteca que nos permite realizar operaciones de archivo de manera asíncrona. Proporciona:
- Versiones asíncronas de las operaciones comunes de archivo
- Métodos para lectura y escritura por líneas o completa
- Manejo asíncrono de archivos

### Instalación
```bash
pip install aiofiles
```

## Operaciones Básicas con aiofiles

### 1. Leer un Archivo Completo
```python
async def leer_archivo(ruta):
    archivo = await aiofiles.open(ruta, 'r')
    contenido = await archivo.read()
    await archivo.close()
    return contenido
```

### 2. Leer un Archivo Línea por Línea
```python
async def leer_lineas(ruta):
    archivo = await aiofiles.open(ruta, 'r')
    for linea in archivo:
        print(linea.strip())
    await archivo.close()
```

### 3. Escribir en un Archivo
```python
async def escribir_archivo(ruta, contenido):
    archivo = await aiofiles.open(ruta, 'w')
    await archivo.write(contenido)
    await archivo.close()
```

### 4. Agregar al Final de un Archivo
```python
async def agregar_linea(ruta, linea):
    archivo = await aiofiles.open(ruta, 'a')
    await archivo.write(linea + '\n')
    await archivo.close()
```

## Ejemplo Práctico: Procesador de Registros

```python
import asyncio
import aiofiles
from datetime import datetime

async def procesar_registro(linea):
    # Simula algún procesamiento
    await asyncio.sleep(0.1)
    return f"[{datetime.now()}] Procesado: {linea}"

async def procesar_archivo_log():
    # Abrir archivo de entrada
    entrada = await aiofiles.open('entrada.log', 'r')
    # Abrir archivo de salida
    salida = await aiofiles.open('procesado.log', 'w')
    
    # Leer y procesar cada línea
    async for linea in entrada:
        resultado = await procesar_registro(linea.strip())
        await salida.write(resultado + '\n')
    
    # Cerrar archivos
    await entrada.close()
    await salida.close()

# Ejecutar
asyncio.run(procesar_archivo_log())
```

## Procesamiento de Múltiples Archivos

Una de las ventajas más importantes de usar operaciones asíncronas es poder trabajar con múltiples archivos simultáneamente:

```python
async def procesar_multiples_archivos(archivos):
    tareas = []
    for archivo in archivos:
        tarea = asyncio.create_task(procesar_archivo(archivo))
        tareas.append(tarea)
    
    # Esperar que todos los archivos se procesen
    resultados = await asyncio.gather(*tareas)
    return resultados
```

## Mejores Prácticas

1. **Manejo de Errores**
```python
async def leer_archivo_seguro(ruta):
    archivo = None
    try:
        archivo = await aiofiles.open(ruta, 'r')
        contenido = await archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"El archivo {ruta} no existe")
        return None
    except Exception as e:
        print(f"Error al leer {ruta}: {e}")
        return None
    finally:
        if archivo:
            await archivo.close()
```

2. **Cierre Adecuado de Archivos**
- Siempre cerrar los archivos usando `await archivo.close()`
- Usar bloques `try/finally` para asegurar que los archivos se cierren incluso si hay excepciones
- Mantener un registro de archivos abiertos para asegurar su cierre

3. **Procesamiento por Lotes**
```python
async def procesar_por_lotes(ruta, tamano_lote=1000):
    archivo = None
    try:
        lineas = []
        archivo = await aiofiles.open(ruta, 'r')
        async for linea in archivo:
            lineas.append(linea)
            if len(lineas) >= tamano_lote:
                await procesar_lote(lineas)
                lineas = []
    finally:
        if archivo:
            await archivo.close()
```

## Ventajas del Manejo Asíncrono de Archivos

1. **Mejor Rendimiento**:
   - No bloquea el programa durante operaciones de I/O
   - Permite procesar múltiples archivos en paralelo
   - Aprovecha mejor los recursos del sistema

2. **Escalabilidad**:
   - Maneja eficientemente grandes cantidades de archivos
   - Ideal para aplicaciones que procesan logs o datos en tiempo real
   - Facilita el procesamiento de archivos en lotes

3. **Responsividad**:
   - El programa permanece receptivo durante operaciones largas
   - Permite mostrar progreso en tiempo real
   - Facilita la cancelación de operaciones en curso

## Conclusión

El manejo asíncrono de archivos es especialmente útil cuando:
- Trabajamos con archivos grandes
- Necesitamos procesar múltiples archivos
- Queremos mantener la aplicación responsiva
- Realizamos operaciones de archivo frecuentes

En el próximo ejercicio, pondremos en práctica estos conceptos creando un sistema de procesamiento de archivos asíncrono. 📝✨
