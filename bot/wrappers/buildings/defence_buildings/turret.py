from .defence_building import DefenceBuilding


class Turret(DefenceBuilding):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
