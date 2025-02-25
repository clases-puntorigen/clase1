# Decoradores en Python: Una Guía Completa

## ¿Qué es un Decorador?

Un decorador es una función en Python que modifica el comportamiento de otra función sin alterar su código directamente. Los decoradores son una forma elegante de aplicar el principio de "envolver" una función con funcionalidad adicional.

## Sintaxis Básica

Los decoradores se aplican usando el símbolo `@` seguido del nombre del decorador, justo encima de la definición de la función que queremos modificar:

```python
@mi_decorador
def mi_funcion():
    pass
```

## Creando un Decorador Simple

### Ejemplo 1: Decorador Básico

```python
def mi_decorador(funcion):
    def wrapper():
        print("Antes de ejecutar la función")
        funcion()
        print("Después de ejecutar la función")
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

# Al llamar a saludar(), veremos:
# Antes de ejecutar la función
# ¡Hola!
# Después de ejecutar la función
saludar()
```

## Decoradores con Argumentos

### Ejemplo 2: Decorador que Maneja Argumentos

```python
def mi_decorador(funcion):
    def wrapper(*args, **kwargs):
        print(f"Argumentos recibidos: {args}, {kwargs}")
        resultado = funcion(*args, **kwargs)
        print(f"La función retornó: {resultado}")
        return resultado
    return wrapper

@mi_decorador
def suma(a, b):
    return a + b

# Al llamar suma(5, 3), veremos:
# Argumentos recibidos: (5, 3), {}
# La función retornó: 8
resultado = suma(5, 3)
```

## Decoradores con Parámetros

### Ejemplo 3: Decorador Configurable

```python
def repetir(veces):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            for _ in range(veces):
                resultado = funcion(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(veces=3)
def saludar(nombre):
    print(f"¡Hola {nombre}!")
    return "OK"

# Al llamar saludar("Juan"), veremos:
# ¡Hola Juan!
# ¡Hola Juan!
# ¡Hola Juan!
saludar("Juan")
```

## Casos de Uso Prácticos

### 1. Medición de Tiempo de Ejecución

```python
import time

def medir_tiempo(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"La función {funcion.__name__} tardó {fin - inicio:.2f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def proceso_pesado():
    time.sleep(2)  # Simula un proceso que tarda 2 segundos
    return "Proceso completado"

# Al llamar proceso_pesado(), veremos:
# La función proceso_pesado tardó 2.00 segundos
```

### 2. Validación de Argumentos

```python
def validar_numeros_positivos(funcion):
    def wrapper(*args, **kwargs):
        if any(arg <= 0 for arg in args):
            raise ValueError("Todos los argumentos deben ser positivos")
        return funcion(*args, **kwargs)
    return wrapper

@validar_numeros_positivos
def calcular_area(largo, ancho):
    return largo * ancho

# Esto funcionará:
area = calcular_area(5, 3)  # Retorna 15

# Esto lanzará un error:
# area = calcular_area(-5, 3)  # ValueError: Todos los argumentos deben ser positivos
```

### 3. Caché de Resultados

```python
def cache_resultados(funcion):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Retornando resultado en caché para {args}")
            return cache[args]
        resultado = funcion(*args)
        cache[args] = resultado
        return resultado
    return wrapper

@cache_resultados
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Primera llamada: calcula todo
print(fibonacci(5))  # Calcula y guarda en caché

# Segunda llamada: usa valores en caché
print(fibonacci(5))  # Usa el valor guardado
```

## Decoradores en Clases

### Ejemplo 4: Decorador de Método

```python
def log_acceso(funcion):
    def wrapper(self, *args, **kwargs):
        print(f"Accediendo al método {funcion.__name__} de {self.__class__.__name__}")
        return funcion(self, *args, **kwargs)
    return wrapper

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
    
    @log_acceso
    def saludar(self):
        return f"¡Hola, soy {self.nombre}!"

usuario = Usuario("Ana")
# Al llamar usuario.saludar(), veremos:
# Accediendo al método saludar de Usuario
# ¡Hola, soy Ana!
```

## Mejores Prácticas

1. **Preservar Metadatos:**
```python
from functools import wraps

def mi_decorador(funcion):
    @wraps(funcion)  # Preserva el nombre y docstring de la función original
    def wrapper(*args, **kwargs):
        return funcion(*args, **kwargs)
    return wrapper
```

2. **Documentación Clara:**
```python
def validar_tipo(tipo):
    """
    Decorador que valida el tipo de los argumentos.
    
    Args:
        tipo: El tipo de dato esperado
    """
    def decorador(funcion):
        @wraps(funcion)
        def wrapper(valor):
            if not isinstance(valor, tipo):
                raise TypeError(f"Se esperaba {tipo.__name__}")
            return funcion(valor)
        return wrapper
    return decorador

@validar_tipo(str)
def procesar_texto(texto):
    """Procesa un texto dado."""
    return texto.upper()
```

## Conclusión

Los decoradores son una herramienta poderosa en Python que permite:
- Modificar el comportamiento de funciones y métodos
- Reutilizar código de manera elegante
- Separar preocupaciones transversales
- Implementar patrones de diseño de manera limpia

Casos comunes de uso incluyen:
- Logging
- Medición de rendimiento
- Validación de entrada
- Caché
- Control de acceso
- Gestión de transacciones

Al usar decoradores, recuerda:
- Mantener la simplicidad
- Documentar el comportamiento
- Preservar los metadatos de las funciones
- Considerar el impacto en el rendimiento
