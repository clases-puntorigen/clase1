import asyncio

async def tarea_1():
    # Imprimir un mensaje de inicio
    # Simular una espera con asyncio.sleep()
    # Imprimir un mensaje de finalización
    print("Esto a comenzado")
    await asyncio.sleep(3)
    print("Termino")

async def tarea_2():
    # Imprimir un mensaje de inicio
    # Simular una espera con asyncio.sleep()
    # Imprimir un mensaje de finalización
    print("comenzando")
    await asyncio.sleep(5)
    print("Terminando")

async def main():
    # Ejecutar ambas tareas en paralelo con asyncio.gather()
    await asyncio.gather(tarea_1(),tarea_2())

# Ejecutar la función principal con asyncio.run()
asyncio.run(main())


