import asyncio
from preparacion import preparacion_plato
from preparacion_jugo import preparacion_jugo
from preparacion_postre import preparacion_postre
async def principal():
    await  asyncio.gather(
        preparacion_plato("papas fritas", 6),
        preparacion_jugo("Melon",3),
        preparacion_postre("helado",5)
    )
asyncio.run(principal())
