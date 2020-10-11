from sc2.ids.unit_typeid import UnitTypeId

from .resource import Resource


class Mineral(Resource):
    id = UnitTypeId.MINERALFIELD

    def __init__(self, bot, *args, **kwargs):
        self._update_source = bot.mineral_field
        super().__init__(bot=bot, *args, **kwargs)

    async def update(self):
        self.minerals_left = self._unit.mineral_contents
