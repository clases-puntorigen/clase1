#!/usr/bin/env python3

"""
Ejercicio: Conversión entre Tipos de Datos en Python

Este ejercicio te ayudará a entender:
- Cómo convertir entre diferentes tipos de datos (str, int, float, list, dict)
- Cómo manejar errores comunes en conversiones
- Cómo trabajar con diferentes formatos de datos
- Cómo validar y limpiar datos antes de convertirlos
"""

def texto_a_numero(texto):
    """
    TODO: Implementa una función que convierta un texto a número (int o float)
    - Si el texto contiene un punto, debe convertirse a float
    - Si el texto es solo números, debe convertirse a int
    - Si el texto no es un número válido, debe retornar None
    
    Ejemplos:
    "123" -> 123 (int)
    "12.5" -> 12.5 (float)
    "abc" -> None
    """
    if not texto:
        return None
    
    try:
        if "." in texto:
            return float(texto)
        return int(texto)
    except:
        return None
        

def lista_a_texto(lista, separador=", "):
    """
    TODO: Implementa una función que convierta una lista a texto
    - Cada elemento debe convertirse a string
    - Los elementos deben unirse usando el separador
    - Si la lista está vacía, retornar ""
    
    Ejemplos:
    [1, 2, 3] -> "1, 2, 3"
    ["a", "b"] -> "a, b"
    [] -> ""
    """
    return separador.join(str(item) for item in lista)
    

def texto_a_lista(texto, separador=","):
    """
    TODO: Implementa una función que convierta un texto a lista
    - El texto debe dividirse por el separador -ok
    - Debe eliminar espacios en blanco al inicio y final de cada elemento
    - Si el texto está vacío, retornar lista vacía -ok
    
    Ejemplos:
    "1, 2     , 3    " -> ["1 ", "2     ", " 3     "]
    "a,b,c" -> ["a", "b", "c"]
    "" -> []
    " dsldslkld sksd          " -> "dsldslkld sksd"
    " dsldslkld sksd          ".strip() -> "dsldslkld sksd"
    """
    if not texto:
        return []
    return [elemento.strip() for elemento in texto.split(separador)]
    

def diccionario_a_lista_tuplas(diccionario):
    """
    TODO: Implementa una función que convierta un diccionario a una lista de tuplas
    - Cada tupla debe contener (llave, valor)
    - La lista debe estar ordenada por llave
    
    Ejemplo:
    {"b": 2, "a": 1} -> [("a", 1), ("b", 2)]
    """
    return sorted(diccionario.items())

def texto_a_diccionario(texto):
    """
    TODO: Implementa una función que convierta un texto a diccionario
    - El texto tiene el formato "llave1=valor1,llave2=valor2"
    - Debe separar por comas y luego por igual
    - Debe eliminar espacios en blanco
    
    Ejemplo:
    ejemplo = "a,b,c,d,e" 
    lista = texto_a_lista(ejemplo)
    lista = ["a","b","c","d","e"]
    for x in lista:
        # x = "a", x = "b", x = "c"
    "nombre=Juan, edad=25" -> {"nombre": "Juan", "edad": "25"}
    strip()
    """
    if not texto:
        return {}
    
    resultado = {}
    elementos = texto_a_lista(texto)
    for elemento in elementos:
        # elemento -> "nombre=Juan" , elemento -> "edad=25", etc..
        llave = elemento.split("=")[0]
        valor = elemento.split("=")[1]
        #llave, valor = elemento.split("=",1)
        resultado[llave.strip()] = valor.strip()
    return resultado
        
def test_texto_a_numero():
    assert texto_a_numero("123") == 123
    assert texto_a_numero("12.5") == 12.5
    assert texto_a_numero("abc") is None
    assert texto_a_numero("") is None

def test_lista_a_texto():
    assert lista_a_texto([1, 2, 3]) == "1, 2, 3"
    assert lista_a_texto(["a", "b"]) == "a, b"
    assert lista_a_texto([]) == ""

def test_texto_a_lista():
    assert texto_a_lista("1, 2, 3") == ["1", "2", "3"]
    assert texto_a_lista("a,b,c") == ["a", "b", "c"]
    assert texto_a_lista("") == []

def test_diccionario_a_lista_tuplas():
    assert diccionario_a_lista_tuplas({"b": 2, "a": 1}) == [("a", 1), ("b", 2)]
    assert diccionario_a_lista_tuplas({}) == []

def test_texto_a_diccionario():
    assert texto_a_diccionario("nombre=Juan, edad=25") == {"nombre": "Juan", "edad": "25"}
    assert texto_a_diccionario("") == {}

def main():
    print("=== Conversión entre Tipos de Datos ===")
    
    # Probar conversión de texto a número
    numero = texto_a_numero("123.45")
    print(f"\nConvertir '123.45' a número: {numero} (tipo: {type(numero).__name__})")
    
    # Probar conversión de lista a texto
    texto = lista_a_texto([1, "dos", 3.0])
    print(f"\nConvertir lista a texto: '{texto}'")
    
    # Probar conversión de texto a lista
    lista = texto_a_lista("manzana, pera, uva")
    print(f"\nConvertir texto a lista: {lista}")
    
    # Probar conversión de diccionario a lista de tuplas
    tuplas = diccionario_a_lista_tuplas({"nombre": "Ana", "edad": "25"})
    print(f"\nConvertir diccionario a tuplas: {tuplas}")
    
    # Probar conversión de texto a diccionario
    diccionario = texto_a_diccionario("ciudad=Santiago, país=Chile")
    print(f"\nConvertir texto a diccionario: {diccionario}")

    # Ejecutar pruebas
    test_texto_a_numero()
    test_lista_a_texto()
    test_texto_a_lista()
    test_diccionario_a_lista_tuplas()
    test_texto_a_diccionario()
    print("\n¡Todas las pruebas pasaron exitosamente!")

if __name__ == "__main__":
    main()
