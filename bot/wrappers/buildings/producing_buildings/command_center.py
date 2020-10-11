from .producing_building import ProducingBuilding


class CommandCenter(ProducingBuilding):
    def __init__(self, *args, **kwargs):
         super().__init__(self, *args, **kwargs)
