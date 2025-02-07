nombreApp = "prueba"

def sumar(a: int,b: int):
    """Suma las dos variables que se le pasan, y devuelve la suma"""
    return a + b

def restar(a: int,b: int):
    """"resta las dos variables que se le pasan, y devueve la resta"""
    return a -b

def multiplicar(a: int,b: int):
    """multiplica las dos variables que se le pasan, y devueve la multiplicacion"""
    return a * b

def division(a:int,b:int):
    """divide las dos variables que se le pasan, y devuelve una division"""
    try:
        return a / b 
    except ZeroDivisionError:
        print("No se puede realizar la division por 0")
    """except TypeError:
        try:
            return int(a) / int(b)
        except:
            print("No se pueden dividir cosas que no son numeros")
    except:
        print("Hubo un error dividiendo")"""
