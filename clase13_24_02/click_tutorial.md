# Tutorial de Click: Creando Interfaces de Línea de Comandos en Python

## ¿Qué es Click?

Click es una biblioteca de Python para crear interfaces de línea de comandos (CLI) de manera elegante y con poco código. A diferencia de usar `print` e `input`, Click ofrece:

- Parseo automático de argumentos
- Validación de tipos
- Documentación automática
- Colores y formato en la terminal
- Manejo de errores robusto
- Subcomandos (como en git)

## Instalación

```bash
pip install click
```

## Ventajas sobre print/input

### Con print/input tradicional:
```python
# Forma tradicional
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
try:
    edad = int(edad)
except ValueError:
    print("Error: La edad debe ser un número")
    exit(1)

print(f"Hola {nombre}, tienes {edad} años")
```

### Con Click:
```python
import click

@click.command()
@click.option('--nombre', prompt='Ingrese su nombre')
@click.option('--edad', type=int, prompt='Ingrese su edad')
def saludar(nombre, edad):
    """Saluda al usuario y muestra su edad."""
    click.echo(f"Hola {nombre}, tienes {edad} años")

if __name__ == '__main__':
    saludar()
```

## Ejemplos Básicos

### 1. Comando Simple con Argumentos

```python
import click

@click.command()
@click.argument('archivo')
def contar_lineas(archivo):
    """Cuenta las líneas en un archivo."""
    try:
        with open(archivo) as f:
            lineas = len(f.readlines())
        click.echo(f'El archivo {archivo} tiene {lineas} líneas')
    except FileNotFoundError:
        click.echo(f'Error: El archivo {archivo} no existe', err=True)
        
if __name__ == '__main__':
    contar_lineas()
```

### 2. Opciones con Valores por Defecto

```python
import click

@click.command()
@click.option('--color', default='azul', help='Tu color favorito')
@click.option('--edad', type=int, default=25, help='Tu edad')
def perfil(color, edad):
    """Muestra el perfil del usuario."""
    click.echo(f'Tu color favorito es {color} y tienes {edad} años')

if __name__ == '__main__':
    perfil()
```

## Ejemplos Intermedios

### 1. Confirmaciones y Entrada Segura

```python
import click

@click.command()
@click.option('--usuario', prompt=True)
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def registrar(usuario, password):
    """Registra un nuevo usuario."""
    if click.confirm(f'¿Crear usuario {usuario}?'):
        click.echo(f'Usuario {usuario} creado exitosamente')
    else:
        click.echo('Operación cancelada')

if __name__ == '__main__':
    registrar()
```

### 2. Colores y Estilos

```python
import click

@click.command()
@click.option('--mensaje', prompt='Escribe un mensaje')
def formatear(mensaje):
    """Muestra un mensaje con diferentes estilos."""
    click.secho('Error: ' + mensaje, fg='red')
    click.secho('Éxito: ' + mensaje, fg='green')
    click.secho('Advertencia: ' + mensaje, fg='yellow')
    click.secho('Info: ' + mensaje, fg='blue', bold=True)

if __name__ == '__main__':
    formatear()
```

## Ejemplos Avanzados

### 1. Grupos de Comandos (Similar a git)

```python
import click

@click.group()
def cli():
    """Suite de herramientas para manejo de archivos."""
    pass

@cli.command()
@click.argument('archivo')
def info(archivo):
    """Muestra información del archivo."""
    import os
    if os.path.exists(archivo):
        stats = os.stat(archivo)
        click.echo(f'Tamaño: {stats.st_size} bytes')
        click.echo(f'Creado: {stats.st_ctime}')
    else:
        click.echo('Archivo no encontrado', err=True)

@cli.command()
@click.argument('archivo')
@click.option('--force', is_flag=True, help='Forzar eliminación')
def eliminar(archivo, force):
    """Elimina un archivo."""
    if not force and not click.confirm(f'¿Eliminar {archivo}?'):
        return
    try:
        import os
        os.remove(archivo)
        click.echo(f'Archivo {archivo} eliminado')
    except FileNotFoundError:
        click.echo('Archivo no encontrado', err=True)

if __name__ == '__main__':
    cli()
```

### 2. Barra de Progreso y Procesamiento

```python
import click
import time

@click.command()
@click.option('--count', default=10, help='Número de elementos a procesar')
def procesar(count):
    """Procesa elementos mostrando una barra de progreso."""
    with click.progressbar(range(count), label='Procesando') as bar:
        for _ in bar:
            # Simula trabajo
            time.sleep(0.1)
    
    # Usando diferentes tipos de spinners
    with click.spinner() as spinner:
        for _ in range(3):
            spinner.write('Trabajando...')
            time.sleep(1)

if __name__ == '__main__':
    procesar()
```

### 3. Entrada/Salida Avanzada

```python
import click

@click.command()
@click.option('--archivo', type=click.File('w'))
@click.option('--verbose', '-v', count=True)
def logger(archivo, verbose):
    """Registra mensajes con diferentes niveles de detalle."""
    niveles = ['ERROR', 'INFO', 'DEBUG']
    nivel = niveles[min(verbose, len(niveles)-1)]
    
    mensaje = click.edit('Escribe tu mensaje aquí')
    if mensaje:
        archivo.write(f'[{nivel}] {mensaje.strip()}\n')
        if click.get_terminal_size()[0] >= 50:
            # Tabla bonita si hay espacio
            click.echo('─' * 50)
            click.echo(f'│ Nivel: {nivel:<10} │ Longitud: {len(mensaje):<10} │')
            click.echo('─' * 50)

if __name__ == '__main__':
    logger()
```

## Mejores Prácticas

1. **Documentación Clara:**
   - Usar docstrings para todos los comandos
   - Proporcionar mensajes de ayuda para las opciones

2. **Manejo de Errores:**
   - Usar `click.echo(mensaje, err=True)` para errores
   - Implementar validaciones apropiadas

3. **Feedback al Usuario:**
   - Usar colores para diferentes tipos de mensajes
   - Mostrar barras de progreso para operaciones largas

4. **Estructura del Código:**
   ```python
   # cli.py
   import click
   
   @click.group()
   @click.option('--debug/--no-debug', default=False)
   @click.pass_context
   def cli(ctx, debug):
       """Herramienta de línea de comandos."""
       ctx.ensure_object(dict)
       ctx.obj['DEBUG'] = debug
   
   @cli.command()
   @click.pass_context
   def comando(ctx):
       """Subcomando con acceso al contexto."""
       if ctx.obj['DEBUG']:
           click.echo('Modo debug activado')
   
   if __name__ == '__main__':
       cli()
   ```

## Conclusión

Click es una herramienta poderosa que:
- Simplifica la creación de CLIs profesionales
- Reduce el código boilerplate
- Mejora la experiencia del usuario
- Facilita el mantenimiento

Úsalo cuando necesites:
- Interfaces de línea de comandos robustas
- Validación de entrada avanzada
- Subcomandos y opciones complejas
- Feedback visual profesional
