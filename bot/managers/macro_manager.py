from loguru import logger as LOG

from .mining_manager import MiningManager

class MacroManager():
    def __init__(self, bot, locations, available_scvs, available_townhalls):
        LOG.info(f"Initializing macromanager for {len(locations)} locations")

        self.bot = bot
        self.mining_managers = list()

        for position, location_data in locations.items():
            new_mining_manager = MiningManager(
                self.bot,
                position,
                location_data,
                minerals=location_data.mineral_field,
                geysers=location_data.vespene_geyser
            )
            self.mining_managers.append(new_mining_manager)

    async def update(self):
        for mining_manager in self.mining_managers:
            await mining_manager.update()
