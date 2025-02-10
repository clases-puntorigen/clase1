#Pide al usuario la base y la altura de un rectángulo y muestra su área.

base = float(input("¿Cual es la base del cuadrado?"))
altura = float(input("¿Cual es la altura del cuadrado?"))

area = base * altura
print(f"El area del cuadrado es: {area}")

#Pide tres notas al usuario y muestra su promedio.

nota1 = float(input("Ingrese su primera nota"))
nota2 = float(input("Ingrese su segunda nota"))
nota3 = float(input("Ingrese su tercera nota"))

final = (nota1 + nota2 + nota3)/3
print(f"El promedio de sus notas es: {final}")

#Pide el precio de un producto y el porcentaje de descuento. Calcula y muestra el precio final después del descuento.

precio = float(input("¿Cual es el precio del producto? "))
porcentaje = int(input("¿Cual es el porcentaje del producto? "))

descuento = (precio * porcentaje)/100
precio_final = precio - descuento

print(f"El precio final del producto es: {precio_final}")


