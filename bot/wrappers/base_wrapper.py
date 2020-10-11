from loguru import logger as LOG

from bot.managers.base_manager import BaseManager

class BaseWrapper:
    _instances = set()

    def __init__(self, tag, bot):
        self.tag = tag
        self.bot = bot
        self._instances.add(self)

    @classmethod
    async def update_subclasses(cls):
        for unit in cls._instances.copy():
            if unit is not None and unit.tag in unit.bot.all_units.tags:
                await unit.update_unit()
                await unit.update()
            else:
                cls._instances.remove(unit)
                BaseManager.unit_destroyed(unit)

    @property
    def position(self):
        return self._unit.position

    async def update_unit(self):
        self._unit = self.bot.all_units.by_tag(self.tag)

    async def update(self):
        raise NotImplementedError("Forgot to override method Update")
