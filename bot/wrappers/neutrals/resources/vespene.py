from sc2.ids.unit_typeid import UnitTypeId

from .resource import Resource


class Vespene(Resource):
    type_id = UnitTypeId.VESPENEGEYSER

    def __init__(self, bot, *args, **kwargs):
        self._update_source = bot.vespene_geyser
        super().__init__(bot=bot, *args, **kwargs)

    @property
    def vespene_left(self):
        return self._unit.vespene_contents
