from loguru import logger as LOG

class MiningManager():
    def __init__(
        self,
        position,
        raw_data,
        townhall=None,
        minerals=None,
        geysers=None,
        workers=None,
    ):
        self.position = position
        self.raw_data = raw_data

        self.townhall = townhall if townhall else None

        self.minerals = minerals if minerals else list()
        self.geysers = geysers if geysers else list()

        self.undistributed_workers = workers if workers else list()

        self.mineral_workers = list()
        self.gas_workers = list()

        pass
