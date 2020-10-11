from .producing_building import ProducingBuilding


class Barracks(ProducingBuilding):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
