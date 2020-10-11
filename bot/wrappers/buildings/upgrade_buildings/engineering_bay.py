from .upgrade_building import UpgradeBuilding


class EngineeringBay(UpgradeBuilding):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
