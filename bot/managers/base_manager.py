class BaseManager():
    _instances = set()

    def __init__(self):
        self._instances.add(self)

    @classmethod
    async def update_subclasses(cls):
        for manager in cls._instances:
            if manager is not None:
                await manager.update()
            else:
                cls._instances.remove(manager)

    @classmethod
    def unit_destroyed(cls, unit):
        for manager in cls._instances:
            if manager is not None:
                manager.remove_unit(unit)

    async def update(self):
        raise NotImplementedError("Forgot to override update method")

    def remove_unit(self, unit):
        raise NotImplementedError("Forgot to clean up units")
