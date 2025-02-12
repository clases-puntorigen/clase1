import asyncio

async def preparacion_jugo(sabor, tiempo):
    print(f"Su jugo de: {sabor}, se encuentra en preparacion y tardara {tiempo} segundos, en estar listo")
    await asyncio.sleep(tiempo)
    print(f"Su jugo de: {sabor} se encuentra listo")
    pass
