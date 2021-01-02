from loguru import logger as log

from bot.managers.base_manager import BaseManager


class Wrappers(type):
    _wrappers = {}

    def __new__(mcs, name, bases, dct):
        wrapper = type.__new__(mcs, name, bases, dct)
        if 'type_id' in dct:
            Wrappers._wrappers[dct['type_id']] = wrapper
        return wrapper

    def set_bot_instance(bot):
        for wrapper in Wrappers._wrappers.values():
            wrapper._bot = bot

    def __class_getitem__(cls, wrapper_key):
        return cls._wrappers[wrapper_key]


class BaseWrapper(object, metaclass=Wrappers):
    _instances = set()

    def __init__(self, tag, bot):
        self.tag = tag
        self.bot = bot
        self._instances.add(self)
        self._unit = self.bot.all_units.by_tag(self.tag)

    @classmethod
    async def update_subclasses(cls):
        for unit in cls._instances.copy():
            if unit is not None and unit.tag in unit.bot.all_units.tags:
                unit.update_unit()
                await unit.update()
            else:
                cls._instances.remove(unit)
                BaseManager.unit_destroyed(unit)

    @property
    def position(self):
        return self._unit.position

    def update_unit(self):
        self._unit = self.bot.all_units.by_tag(self.tag)

    async def update(self):
        pass
