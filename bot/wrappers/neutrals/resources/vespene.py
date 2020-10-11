from sc2.ids.unit_typeid import UnitTypeId

from .resource import Resource


class Vespene(Resource):
    id = UnitTypeId.VESPENEGEYSER

    def __init__(self, bot, *args, **kwargs):
        self._update_source = bot.vespene_geyser
        super().__init__(bot=bot, *args, **kwargs)

    async def update(self):
        self.vespene_left = self._unit.vespene_contents
