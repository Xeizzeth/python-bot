from .mining_manager import MiningManager

class MacroManager():
    def __init__(self, locations, available_scvs, available_townhalls):
        for position, location_data in locations.items():
            new_mining_manager = MiningManager(
                position,
                location_data,
                minerals=location_data.mineral_field,
                geysers=locations.vespene_geyser
            )
