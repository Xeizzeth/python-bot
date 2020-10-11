from loguru import logger as LOG

from .base_manager import BaseManager

from .mining_manager import MiningManager

class MacroManager(BaseManager):
    def __init__(self, bot, locations, available_scvs, available_townhalls):
        super().__init__()
        LOG.info(f"Initializing macromanager for {len(locations)} locations")

        self.bot = bot
        self.mining_managers = list()

        for position, location_data in locations.items():
            new_mining_manager = MiningManager(
                bot=self.bot,
                position=position,
                raw_data=location_data,
                mineral_tags=location_data["mineral_tags"],
                vespene_tags=location_data["vespene_tags"]
            )
            self.mining_managers.append(new_mining_manager)

    async def update(self):
        pass

    def remove_unit(self, unit):
        pass