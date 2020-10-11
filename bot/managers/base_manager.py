import weakref

class BaseManager():
    _instances = set()

    def __init__(self):
        self._instances.add(weakref.ref(self))

    @classmethod
    async def update_subclasses(cls):
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                await obj.update()
            else:
                cls._instances.remove(ref)

    def update(self):
        pass
