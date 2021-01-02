from sc2.ids.unit_typeid import UnitTypeId

from .producing_building import ProducingBuilding


class CommandCenter(ProducingBuilding):
    type_id = UnitTypeId.COMMANDCENTER

    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
