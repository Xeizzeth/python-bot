from sc2.ids.unit_typeid import UnitTypeId

from .resource import Resource


class Mineral(Resource):
    type_id = UnitTypeId.MINERALFIELD

    def __init__(self, bot, *args, **kwargs):
        super().__init__(bot=bot, *args, **kwargs)

    @property
    def minerals_left(self):
        return self._unit.mineral_contents
