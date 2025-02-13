# Tutorial: El Administrador de Contexto `with` en Python

## ¿Qué es el `with`?

El `with` es un administrador de contexto que nos ayuda a manejar recursos de manera segura y limpia. Es especialmente útil para:
- Archivos
- Conexiones de red
- Bases de datos
- Cualquier recurso que necesite ser liberado después de su uso

## ¿Por qué usar `with`?

### Sin usar `with` (forma problemática) ❌
```python
# Manera incorrecta de manejar archivos
archivo = open('datos.txt', 'r')
contenido = archivo.read()
# ¿Qué pasa si ocurre un error antes de cerrar?
archivo.close()  # Podríamos olvidar cerrar el archivo
```

### Usando `with` (forma correcta) ✅
```python
# Manera correcta y segura
with open('datos.txt', 'r') as archivo:
    contenido = archivo.read()
# El archivo se cierra automáticamente, incluso si hay errores
```

## Beneficios del `with`

1. **Gestión Automática**: 
   - Libera recursos automáticamente
   - No necesitas recordar cerrar archivos o conexiones

2. **Manejo de Errores**:
   - Garantiza la limpieza incluso si ocurren errores
   - Previene fugas de recursos

3. **Código más Limpio**:
   - Más legible
   - Menos propenso a errores
   - Sigue el principio RAII (Resource Acquisition Is Initialization)

## Ejemplos Prácticos

### 1. Trabajando con Archivos
```python
# Lectura
with open('entrada.txt', 'r') as archivo:
    datos = archivo.read()

# Escritura
with open('salida.txt', 'w') as archivo:
    archivo.write('Hola Mundo')

# Múltiples archivos
with open('origen.txt', 'r') as entrada, \
     open('destino.txt', 'w') as salida:
    contenido = entrada.read()
    salida.write(contenido)
```

### 2. Conexiones de Red
```python
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('ejemplo.com', 80))
    s.sendall(b'GET / HTTP/1.0\r\n\r\n')
    respuesta = s.recv(1024)

```

### 3. Bases de Datos
```python
import sqlite3

with sqlite3.connect('base_datos.db') as conexion:
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios')
    datos = cursor.fetchall()
```

## Creando Nuestros Propios Administradores de Contexto

### 1. Usando una Clase
```python
class MiContexto:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __enter__(self):
        print(f"Iniciando {self.nombre}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Finalizando {self.nombre}")
        # Manejar cualquier limpieza necesaria

# Uso
with MiContexto("ejemplo") as ctx:
    print("Haciendo algo...")
```

### 2. Usando el Decorador contextlib
```python
from contextlib import contextmanager

@contextmanager
def temporizador():
    from time import time
    inicio = time()
    yield  # Aquí se ejecuta el código dentro del with
    fin = time()
    print(f"Tiempo transcurrido: {fin - inicio:.2f} segundos")

# Uso
with temporizador():
    # Código a medir
    for i in range(1000000):
        pass
```

## Casos de Uso Comunes

### 1. Cambio Temporal de Directorio
```python
import os
from contextlib import contextmanager

@contextmanager
def cambiar_directorio(ruta):
    #os.getcwd() = current working directory
    directorio_actual = os.getcwd()
    try:
        #ch = change directory
        os.chdir(ruta)
        yield
    finally:
        os.chdir(directorio_actual)

# Uso
with cambiar_directorio('/tmp'):
    # Trabajar en /tmp
    pass
# Volvemos automáticamente al directorio original
```

### 2. Medición de Rendimiento
```python
from contextlib import contextmanager
from time import time

@contextmanager
def medir_tiempo(descripcion):
    inicio = time()
    try:
        yield
    finally:
        tiempo = time() - inicio
        print(f"{descripcion}: {tiempo:.2f} segundos")

# Uso
with medir_tiempo("Operación costosa"):
    # Código a medir
    resultado = sum(range(10**7))
```

## Mejores Prácticas

1. **Siempre usar `with` para recursos**:
   - Archivos
   - Conexiones
   - Locks (bloqueos)
   - Cualquier objeto que necesite limpieza

2. **Manejar Múltiples Recursos**:
   ```python
   with contexto1() as ctx1, \
        contexto2() as ctx2:
       # Usar ctx1 y ctx2
   ```

3. **Documentar Comportamiento**:
   - Si creas tu propio administrador de contexto
   - Especificar qué recursos se manejan
   - Explicar qué ocurre al entrar y salir

## Ejercicios Sugeridos

1. Crear un administrador de contexto para:
   - Medir tiempo de ejecución
   - Manejar conexiones a bases de datos
   - Cambiar configuraciones temporalmente

2. Practicar con archivos:
   - Leer y escribir
   - Copiar contenido
   - Procesar línea por línea

3. Implementar patrones comunes:
   - Backup y restauración
   - Logging temporal
   - Cambios de configuración

## Conclusión

El `with` es una herramienta poderosa que:
- Hace el código más seguro
- Reduce errores comunes
- Mejora la legibilidad
- Garantiza la limpieza de recursos

En el próximo ejercicio, practicaremos creando nuestros propios administradores de contexto. 🔧✨
