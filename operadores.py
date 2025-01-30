#!/usr/bin/env python3

"""
Ejercicio 8: Operadores en Python

Este ejercicio te ayudará a entender:
- Operadores aritméticos (suma, resta, etc.)
- Operadores de comparación (mayor que, menor que, etc.)
- Operadores lógicos (and, or, not)
- Operadores de asignación (=, +=, -=, etc.)
"""

def calcular_precio_con_descuento(precio_original, porcentaje_descuento):
    """
    TODO: Calcula el precio final después de aplicar un descuento.
    
    Por ejemplo:
    calcular_precio_con_descuento(1000, 20) -> 800
    (1000 - (1000 * 0.20))
    descuento = (1000 * 0.20)
    precio_final = 1000 - descuento
    
    PISTA: Usa el operador * para calcular el descuento
    y el operador - para restarlo del precio original
    """
    descuento = precio_original * (porcentaje_descuento/100)
    precio_final = precio_original - descuento
    return precio_final
     

def es_edad_valida(edad):
    """
    TODO: Verifica si una edad es válida (entre 0 y 120 años).
    
    Por ejemplo:
    es_edad_valida(25) -> True
    es_edad_valida(-5) -> False
    es_edad_valida(200) -> False
    
    PISTA: Usa los operadores >= y <= junto con and
    """
    if edad >= 0 and edad <=120:
        return True
    else:
        return False
        
def calcular_siguiente_nivel(nivel_actual, puntos):
    """
    TODO: Calcula si un jugador puede subir de nivel.
    Sube de nivel si:
    - Su nivel actual es menor que 10
    - Tiene 100 puntos o más
    
    Por ejemplo:
    calcular_siguiente_nivel(5, 100) -> 6
    calcular_siguiente_nivel(5, 80) -> 5
    calcular_siguiente_nivel(10, 200) -> 10
    
    PISTA: Usa los operadores < y >= con and, luego += si sube de nivel
    """
    if nivel_actual < 10 and puntos >= 100:
        nivel_actual += 1        
    return nivel_actual
     
def ajustar_temperatura(temperatura_actual, temperatura_deseada):
    """
    TODO: Indica cómo ajustar un termostato.
    Debe retornar:
    - "calentar" si la temperatura actual es menor que la deseada
    - "enfriar" si la temperatura actual es mayor que la deseada
    - "mantener" si son iguales
    
    Por ejemplo:
    ajustar_temperatura(20, 25) -> "calentar"
    ajustar_temperatura(25, 20) -> "enfriar"
    ajustar_temperatura(22, 22) -> "mantener"
    
    PISTA: Usa los operadores <, > e == con if-elif-else
    """
    if temperatura_actual < temperatura_deseada:
        return "calentar"
    elif temperatura_actual > temperatura_deseada:
        return "enfriar"
    else:
        return "mantener"
    
    

def verificar_acceso(es_admin, esta_logueado, modo_mantenimiento):
    """
    TODO: Verifica si un usuario puede acceder al sistema.
    Puede acceder si:
    - Es administrador, o
    - Está logueado y el sistema NO está en mantenimiento
    
    Por ejemplo:
    verificar_acceso(True, False, True) -> True
    verificar_acceso(False, True, False) -> True
    verificar_acceso(False, True, True) -> False
    
    PISTA: Usa los operadores or, and y not
    """
    return es_admin or (esta_logueado and not modo_mantenimiento)

def main():
    # Prueba 1: Cálculo de descuentos
    print("=== Descuentos ===")
    productos = [(1000, 20), (500, 10), (2000, 50)]
    for precio, descuento in productos:
        precio_final = calcular_precio_con_descuento(precio, descuento)
        print(f"Precio: ${precio}, Descuento: {descuento}%, Final: ${precio_final}")
    
    # Prueba 2: Verificación de edades
    print("\n=== Edades ===")
    edades = [-5, 0, 25, 120, 200]
    for edad in edades:
        es_valida = es_edad_valida(edad)
        print(f"Edad: {edad} años -> {'Válida' if es_valida else 'No válida'}")
    
    # Prueba 3: Subida de nivel
    print("\n=== Niveles ===")
    casos = [(5, 100), (5, 80), (10, 200)]
    for nivel, puntos in casos:
        nuevo_nivel = calcular_siguiente_nivel(nivel, puntos)
        print(f"Nivel: {nivel}, Puntos: {puntos} -> Nuevo nivel: {nuevo_nivel}")
    
    # Prueba 4: Control de temperatura
    print("\n=== Temperatura ===")
    casos = [(20, 25), (25, 20), (22, 22)]
    for actual, deseada in casos:
        accion = ajustar_temperatura(actual, deseada)
        print(f"Actual: {actual}°C, Deseada: {deseada}°C -> {accion}")
    
    # Prueba 5: Verificación de acceso
    print("\n=== Control de Acceso ===")
    casos = [
        (True, False, True),
        (False, True, False),
        (False, True, True),
        (False, False, False)
    ]
    for admin, logueado, mantenimiento in casos:
        acceso = verificar_acceso(admin, logueado, mantenimiento)
        print(f"Admin: {admin}, Logueado: {logueado}, "
              f"Mantenimiento: {mantenimiento} -> "
              f"{'Acceso permitido' if acceso else 'Acceso denegado'}")

if __name__ == "__main__":
    main()
