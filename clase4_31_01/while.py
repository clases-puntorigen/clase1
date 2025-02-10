numero = 1
continuar = True
while continuar:
    print(f"numero es: {numero}")
    numero += 1
    if numero % 10 == 0:
        print("--- cambiando pagina ---")
    elif numero >= 100:
        continuar = False
