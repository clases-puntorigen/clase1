import asyncio

async def preparacion_postre(nombre_postre,tiempo):
    print(f"Su postre de: {nombre_postre}, tardara {tiempo} segundos en estar listo")
    await asyncio.sleep(tiempo)
    print(f"Su {nombre_postre}, se encuentra listo")
    