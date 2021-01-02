from sc2.ids.unit_typeid import UnitTypeId

from .worker import Worker


class Scv(Worker):
    type_id = UnitTypeId.SCV

    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
