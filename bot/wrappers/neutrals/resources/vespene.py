from sc2.ids.unit_typeid import UnitTypeId

from .resource import Resource


class Vespene(Resource):
    type_id = UnitTypeId.VESPENEGEYSER

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def vespene_left(self):
        return self._unit.vespene_contents
