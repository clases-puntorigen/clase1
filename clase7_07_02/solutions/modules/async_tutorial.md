# Tutorial: Programación Asíncrona en Python con async/await

## ¿Qué es la programación asíncrona?

Imagina que estás haciendo un sandwich 🥪. En un enfoque **síncrono** (tradicional), harías cada paso en orden:
1. Tostar el pan (2 minutos)
2. Cortar el tomate (1 minuto)
3. Cortar el queso (1 minuto)

Tiempo total: 4 minutos, porque haces todo en secuencia.

En un enfoque **asíncrono**, mientras el pan se tuesta (tarea que no requiere tu atención constante), podrías estar cortando el tomate y el queso.
Tiempo total: ¡2 minutos! Porque aprovechas el tiempo de espera para hacer otras tareas.

## ¿Por qué usar async/await?

La programación asíncrona es útil cuando tu programa:
- Hace muchas operaciones de entrada/salida (I/O)
- Necesita esperar respuestas de servidores
- Realiza múltiples tareas que incluyen tiempos de espera
- Debe mantener una interfaz responsiva mientras procesa datos

## Conceptos Básicos

### 1. Funciones Asíncronas

Una función asíncrona se define con `async def` y puede usar `await`:

```python
# Función tradicional
def saludar():
    return "¡Hola!"

# Función asíncrona
async def saludar_async():
    return "¡Hola!"
```

### 2. La palabra clave `await`

`await` le dice a Python: "espera a que esta operación termine, pero mientras tanto puedes hacer otras cosas":

```python
import asyncio

async def preparar_cafe():
    print("Calentando agua...")
    await asyncio.sleep(2)  # Simula espera de 2 segundos
    return "¡Café listo! ☕"
```

## La Biblioteca asyncio

`asyncio` es la biblioteca estándar de Python para escribir código asíncrono usando la sintaxis `async`/`await`. Esta biblioteca proporciona:
- Un bucle de eventos (event loop) que maneja la ejecución de tareas asíncronas
- Herramientas para gestionar concurrencia
- Funciones para trabajar con tareas asíncronas

### Métodos Principales de asyncio

1. **asyncio.run()**
```python
asyncio.run(funcion_principal())
```
- Es la forma principal de ejecutar código asíncrono
- Crea el bucle de eventos y lo gestiona automáticamente
- Se usa una sola vez en el programa, típicamente en el punto de entrada

2. **asyncio.gather()**
```python
resultados = await asyncio.gather(tarea1(), tarea2(), tarea3())
```
- Ejecuta múltiples tareas en paralelo
- Espera a que todas las tareas terminen
- Retorna una lista con los resultados de todas las tareas
- Muy útil para ejecutar varias operaciones simultáneamente

3. **asyncio.sleep()**
```python
await asyncio.sleep(2)  # Espera 2 segundos
```
- Pausa la ejecución sin bloquear otras tareas
- Útil para simular operaciones que toman tiempo
- Versión asíncrona de time.sleep()

4. **asyncio.create_task()**
```python
tarea = asyncio.create_task(mi_funcion_async())
```
- Programa una corrutina para su ejecución
- Retorna un objeto Task que podemos esperar más tarde
- Útil para iniciar tareas en segundo plano

### Ejemplo Práctico con asyncio

```python
import asyncio

async def procesar_dato(id: int):
    print(f"Iniciando procesamiento {id}")
    await asyncio.sleep(1)  # Simula trabajo
    return f"Dato {id} procesado"

async def main():
    # Crear varias tareas
    tareas = [
        asyncio.create_task(procesar_dato(i))
        for i in range(3)
    ]
    
    # Esperar que todas terminen
    resultados = await asyncio.gather(*tareas)
    print(resultados)

# Ejecutar el programa
asyncio.run(main())
```

### Patrones Comunes con asyncio

1. **Procesamiento Paralelo**
```python
async def procesar_varios():
    return await asyncio.gather(
        tarea_larga_1(),
        tarea_larga_2(),
        tarea_larga_3()
    )
```

2. **Timeout (tiempo límite)**
```python
try:
    async with asyncio.timeout(2):  # Espera máximo 2 segundos
        await operacion_larga()
except asyncio.TimeoutError:
    print("La operación tomó demasiado tiempo")
```

3. **Tareas en Segundo Plano**
```python
# Iniciar tarea sin esperar resultado inmediato
tarea_bg = asyncio.create_task(actualizar_datos())
# Hacer otras cosas...
await tarea_bg  # Esperar cuando necesitemos el resultado
```

## Ejemplo Simple: Descargando Imágenes

Comparemos los dos enfoques:

### Enfoque Síncrono (Tradicional) ⏰

```python
def descargar_foto(nombre):
    print(f"Descargando {nombre}...")
    time.sleep(2)  # Simula tiempo de descarga
    print(f"¡{nombre} descargada!")

# Descargar 3 fotos
for foto in ["foto1.jpg", "foto2.jpg", "foto3.jpg"]:
    descargar_foto(foto)

# Tiempo total: 6 segundos
```

### Enfoque Asíncrono (Moderno) ⚡

```python
async def descargar_foto_async(nombre):
    print(f"Descargando {nombre}...")
    await asyncio.sleep(2)  # Simula tiempo de descarga
    print(f"¡{nombre} descargada!")

# Descargar 3 fotos simultáneamente
async def descargar_todas():
    tareas = [
        descargar_foto_async(foto)
        for foto in ["foto1.jpg", "foto2.jpg", "foto3.jpg"]
    ]
    await asyncio.gather(*tareas)

# Tiempo total: ¡solo 2 segundos!
```

## Reglas Importantes

1. Solo puedes usar `await` dentro de funciones `async`
2. Las funciones `async` siempre devuelven un objeto especial llamado "coroutine"
3. Para ejecutar código asíncrono, necesitas usar:
   ```python
   asyncio.run(funcion_principal())
   ```

## Ejemplo Práctico: Bot de Cocina 🤖

Veamos un ejemplo simple antes de hacer el ejercicio del restaurante:

```python
import asyncio

async def calentar_agua(taza):
    print(f"Calentando agua para {taza}...")
    await asyncio.sleep(2)
    return f"Agua caliente para {taza} lista!"

async def preparar_te():
    # Calentar agua para 3 tazas simultáneamente
    tazas = ["taza1", "taza2", "taza3"]
    resultados = await asyncio.gather(*[
        calentar_agua(taza) for taza in tazas
    ])
    
    for resultado in resultados:
        print(resultado)

# Ejecutar
asyncio.run(preparar_te())
```

Este código calentará agua para tres tazas al mismo tiempo, ¡no una después de la otra!

## Beneficios Principales

1. **Mejor Rendimiento**: Realiza múltiples tareas en menos tiempo
2. **Eficiencia**: Aprovecha los tiempos de espera para hacer otras tareas
3. **Responsividad**: Tu programa puede seguir respondiendo mientras espera
4. **Escalabilidad**: Maneja más tareas simultáneas sin bloquear el programa

## Conclusión

La programación asíncrona con async/await nos permite:
- Escribir código que parece síncrono (fácil de leer)
- Pero se ejecuta de manera asíncrona (eficiente)
- Perfecto para tareas que involucran espera (red, archivos, etc.)

Ahora que entiendes los conceptos básicos, ¡estás listo para el ejercicio del restaurante! 🎉

## Recursos Adicionales
- [Documentación oficial de asyncio](https://docs.python.org/es/3/library/asyncio.html)
- [Tutorial de Python sobre async/await](https://realpython.com/async-io-python/)
