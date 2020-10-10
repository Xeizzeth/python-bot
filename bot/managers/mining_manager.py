from loguru import logger as LOG

class MiningManager():
    def __init__(
        self,
        bot,
        position,
        raw_data,
        townhall=None,
        minerals=None,
        geysers=None,
        workers=None,
    ):
        self.bot = bot

        self.position = position
        self.raw_data = raw_data

        self.townhall = townhall if townhall else None

        self.minerals = minerals if minerals else list()
        self.geysers = geysers if geysers else list()

        self.undistributed_workers = workers if workers else list()

        self.mineral_workers = list()
        self.gas_workers = list()

    async def update(self):
        await self.draw_debug_info()

    async def draw_debug_info(self):
        entries = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten"
        ]

        self.bot.draw_sphere(self.position, 2.5)
        self.bot.draw_text_info(entries, self.position)

        for mineral in self.minerals:
            self.bot.draw_sphere(
                mineral.position,
                color=(0, 255, 255)
            )
            self.bot.draw_text_info(
                entries=entries[:2],
                position=mineral.position,
                x_offset=0.5
            )

        for geyser in self.geysers:
            self.bot.draw_sphere(
                geyser.position,
                radius=1.5,
                color=(0, 255, 0)
            )
            self.bot.draw_text_info(
                entries=entries[:6],
                position=geyser.position,
                x_offset=1.5
            )
