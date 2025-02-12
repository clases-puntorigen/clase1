import asyncio

"""
Instrucciones
Define una función asíncrona que reciba el nombre del pedido y el tiempo de preparación.
Usa await asyncio.sleep() para simular el tiempo de espera.
Muestra mensajes indicando cuándo inicia y termina cada pedido.
Crea una función principal que ejecute varios pedidos en paralelo usando asyncio.gather().
Llama a asyncio.run() para ejecutar la función principal.

Pistas
Usa async def para definir funciones asíncronas.
Usa await asyncio.sleep(segundos) para simular la preparación.
Usa asyncio.gather() para manejar múltiples pedidos simultáneamente.

"""
async def preparacion(nombre,tiempo):
    print(f"Su plato {nombre}, se encuentra en preparacion y tardara {tiempo} segundos, en estar listo")
    await asyncio.sleep(tiempo)
    print(f"Su plato: {nombre} se encuentra listo")

async def principal():
    await asyncio.gather(
        preparacion("Pizza", 5),
        preparacion("Pasta", 3),
        preparacion("Ensalada", 2)   
    )

asyncio.run(principal())




