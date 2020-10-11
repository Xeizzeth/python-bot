from bot.wrappers.buildings.building import Building


class ProducingBuilding(Building):
    def __init__(self, *args, **kwargs):
         super().__init__(self, *args, **kwargs)
