from loguru import logger as LOG

from .mining_manager import MiningManager

class MacroManager():
    def __init__(self, locations, available_scvs, available_townhalls):
        LOG.debug("hello world from MACRO manager")
        for position, location_data in locations.items():
            new_mining_manager = MiningManager(
                position,
                location_data,
                minerals=location_data.mineral_field,
                geysers=location_data.vespene_geyser
            )
