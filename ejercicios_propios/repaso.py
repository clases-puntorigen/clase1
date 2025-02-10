numeros = [1,2,3,4,5,6,7,8,9,10]
pares = [n for n in numeros if n % 2 == 0]
print(pares)

palabras = {"hola", "hola2", "hola3"}
diccionario = {palabra: len(palabra) for palabra in palabras}
print(diccionario)

#listas
lista = [1,2,3,True]
print(lista[0])
print(lista[1:3])

# cambiar elemento
lista[2] = [60]

# append -> agregar al ultimo
lista.append(12)
#index -> devuelve donde aparece un elemento la primera vez
lista.index(12)


#tuplas no se puede modificar, son importantes para el orden de los elementos
nombre_completo = ("jose","hola")
nombre,apellido = nombre_completo
print(nombre)
print(apellido)
print(nombre_completo[1:3])

# las tuplas se pueden juntar con el signo +
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print(tupla1 + tupla2)

#una tupla para poder agregarle elementos, se puede convertir en lista asi:
mi_tupla = (1, 2, 3)
lista = list(mi_tupla) 


#lambda
#variable = lambda argumento : expresion 

sumar = lambda n1,n2,n3: n1 + n2 + n3
print(sumar(12,12,12))

# conertir texto a numero
numero_entero = int("25")
print(numero_entero)       
print(type(numero_entero))

#covetir de numero a texto
edad = 30
texto = str(edad)
print(texto)              
print(type(texto)) 











# try
#try:
# Código que puede generar una excepción
#except:
# Código que maneja la excepción (si ocurre)
#else:
# Código que se ejecuta si no ocurre ninguna excepción
#finally:
# Código que se ejecuta siempre, haya o no habido excepción

