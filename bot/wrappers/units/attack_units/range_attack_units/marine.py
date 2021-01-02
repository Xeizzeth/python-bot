from sc2.ids.unit_typeid import UnitTypeId

from .range_attack_unit import RangeAttackUnit


class Marine(RangeAttackUnit):
    type_id = UnitTypeId.MARINE

    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
