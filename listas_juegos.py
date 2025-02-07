#!/usr/bin/env python3

"""
Ejercicio: Introducción a las Listas en Python

Este ejercicio te ayudará a entender:
- Cómo crear y manipular listas
- Operaciones básicas con listas (agregar, insertar, eliminar elementos)
- Acceso a elementos por índice
- Trabajo con múltiples listas
- Operaciones de búsqueda y cálculos con listas
"""
notas_jose = [4.0,5.8,6.0,6.4,6.7,3.9]
promedio = sum(notas_jose) / len(notas_jose)
print(f"El promedio de Jose era {promedio}")


# TODO: Crea una lista llamada 'videojuegos' con al menos 5 nombres de juegos en español
# Ejemplo: ['Los Sims 4', 'Minecraft', 'FIFA 23', ...]
videojuegos = ['valoranrt', 'minecraft','fortnite','lol','mortal kombat']

# TODO: Crea una lista llamada 'precios' con los precios de los juegos anteriores
# Los precios deben ser números decimales (float)
# Ejemplo: [45000.0, 29990.0, 69990.0, ...]
precios = [2000.0, 12000.0, 10000.0, 5600.0, 7800.0]
print(f"Si quiero llevar todos los juegos, tengo que pagar ${sum(precios)}")
print(f"Hay {len(videojuegos)} cantidad de juegos")

print(f"Juego {videojuegos[0]} cuesta ${precios[0]}")
print(f"El precio mas caro es: {max(precios)}")
posicion_por_precio = precios.index(12000.0)
print(f"cual cuesta 12000 ? {videojuegos[posicion_por_precio]}")

#nombre_juego2 = lambda precio: videojuegos[precios.index(precio)]

def devuelve_tuple(nombre, edad):
    return (nombre, edad)

def nombre_juego_x_precio(precio):
    try:
        return videojuegos[precios.index(precio)]
    except:
        print(f"No hay un producto con el precio de {precio}")
        return ""

print(f"JUEGO: {nombre_juego_x_precio(9000)}")
name, age = devuelve_tuple("Jose",20)
print(f"cosa {name} y {age}")

def obtener_juego_mas_caro(juegos, precios):
    """
    TODO: Implementa una función que reciba dos listas (juegos y precios)
    y retorne una tupla con el nombre del juego más caro y su precio
    """
    #juegos = ['valoranrt', 'minecraft','fortnite','lol','mortal kombat']
    #precios = [2000.0, 12000.0, 10000.0, 5600.0, 7800.0]
    precio_mas_caro = max(precios)
    #precio_mas_caro = 12000.0
    indice = precios.index(precio_mas_caro)
    #indice = 1
    nombre_juego = juegos[indice]
    #nombre_juego = juegos[1]
    #nombre_juego = "minecraft"
    return (nombre_juego, precio_mas_caro)
    #return ("mineecraft", 12000.0)

def calcular_precio_promedio(precios):
    """
    TODO: Implementa una función que calcule y retorne el precio promedio
    de todos los juegos
    """
    promedio_precios = sum(precios) / len(precios)
    return promedio_precios
    
def obtener_juegos_caros(juegos, precios, precio_minimo):
    """
    TODO: Implementa una función que retorne una lista con los nombres
    de los juegos que cuestan más que precio_minimo
    """
    

def test_obtener_juego_mas_caro():
    juegos = ['Juego 1', 'Juego 2', 'Juego 3']
    precios = [1000.0, 2000.0, 3000.0]
    juego_mas_caro, precio_mas_alto = obtener_juego_mas_caro(juegos, precios)
    assert juego_mas_caro == 'Juego 3'
    assert precio_mas_alto == 3000.0

def test_calcular_precio_promedio():
    precios = [1000.0, 2000.0, 3000.0]
    promedio = calcular_precio_promedio(precios)
    assert promedio == 2000.0

def test_obtener_juegos_caros():
    juegos = ['Juego 1', 'Juego 2', 'Juego 3']
    precios = [1000.0, 2000.0, 3000.0]
    juegos_caros = obtener_juegos_caros(juegos, precios, 1500.0)
    assert juegos_caros == ['Juego 2', 'Juego 3']

def main():
    # Probando la manipulación básica de listas
    print("=== Lista de Videojuegos ===")
    print(f"Primer juego: {videojuegos[0]}")
    print(f"Último juego: {videojuegos[-1]}")
    
    # TODO: Agrega un nuevo juego al final de la lista usando append()
    # TODO: Inserta un juego en la posición 2 usando insert()
    # TODO: Elimina el último juego de la lista usando pop()
    
    print("\n=== Análisis de Precios ===")
    juego_mas_caro, precio_mas_alto = obtener_juego_mas_caro(videojuegos, precios)
    print(f"Juego más caro: {juego_mas_caro} (${precio_mas_alto})")
    
    promedio = calcular_precio_promedio(precios)
    print(f"Precio promedio: ${promedio:.2f}")
    
    juegos_caros = obtener_juegos_caros(videojuegos, precios, 15000)
    print("\nJuegos que cuestan más de $15000:")
    for juego in juegos_caros:
        print(f"- {juego}")

    # Ejecutar pruebas
    test_obtener_juego_mas_caro()
    test_calcular_precio_promedio()
    test_obtener_juegos_caros()
    print("\n¡Todas las pruebas pasaron exitosamente!")

if __name__ == "__main__":
    pass
    main()
