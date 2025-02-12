import asyncio

async def preparacion_plato(nombre, tiempo):
    print(f"Su plato {nombre}, se encuentra en preparacion y tardara {tiempo} segundos, en estar listo")
    await asyncio.sleep(tiempo)
    print(f"Su plato: {nombre} se encuentra listo")
    pass
