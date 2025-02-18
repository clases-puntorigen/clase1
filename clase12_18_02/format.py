# Tutorial: Método format() en strings
# Este tutorial explica cómo usar el método format() para formatear strings en Python

nombre = "Jose"
edad = 25
print("Hola "+nombre+", tu edad es "+str(edad))
print(f"Hola {nombre}, tu edad es {edad}")

# 1. Formato básico con posición
nombre = "Ana"
edad = 25
print("Ejemplo 1 - Formato básico:")
mensaje = "Hola {}, tienes {} años".format(nombre, edad)
print(mensaje)
print()

# 2. Formato con índices
print("Ejemplo 2 - Formato con índices:")
mensaje = "El orden puede cambiar: {1} tiene {0} años".format(edad, nombre)
print(mensaje)
print()

# 3. Formato con nombres
print("Ejemplo 3 - Formato con nombres:")
mensaje = "Datos: {n} tiene {e} años".format(n=nombre, e=edad)
print(mensaje)
print()

# 4. Formato con números
precio = 19.99
cantidad = 3
print("Ejemplo 4 - Formato con números:")
mensaje = "Total: ${:.2f} por {} unidades".format(precio, cantidad)
print(mensaje)
print()

# 5. Formato con diccionarios
datos = {"nombre": "Carlos", "profesion": "ingeniero"}
print("Ejemplo 5 - Formato con diccionarios:")
mensaje = "{nombre} trabaja como {profesion}".format(**datos)
print(mensaje)
print()

# 6. Alineación y relleno
print("Ejemplo 6 - Alineación y relleno:")
for num in range(1, 4):
    print("Número: {:>3}".format(num))  # Alineación derecha con 3 espacios
print()

# 7. Formato con tipos específicos
binario = 42
print("Ejemplo 7 - Formato con tipos específicos:")
mensaje = """
Número: {}
Binario: {:b}
Hexadecimal: {:x}
""".format(binario, binario, binario)
print(mensaje)

# Nota: A partir de Python 3.6+, se pueden usar f-strings como alternativa más moderna:
# nombre = "Ana"
# mensaje = f"Hola {nombre}"