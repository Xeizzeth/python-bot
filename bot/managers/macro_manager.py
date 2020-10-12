from loguru import logger as LOG

from sc2.ids.unit_typeid import UnitTypeId

from .base_manager import BaseManager
from .mining_manager import MiningManager

from bot.wrappers.buildings import (
    CommandCenter,
    # Nexus # TODO: NOT IMPLEMENTED YET
    # Hatchery # TODO: NOT IMPLEMENTED YET
)
from bot.wrappers.units import (
    Scv,
    # Probe # TODO: NOT IMPLEMENTED YET
    # Drone # TODO: NOT IMPLEMENTED YET
)

class MacroManager(BaseManager):
    def __init__(
        self,
        bot,
        locations=None,
        worker_tags=None,
        townhall_tags=None
    ):
        super().__init__()
        LOG.info(f"Initializing macromanager for {len(locations)} locations")

        self.bot = bot
        self.mining_managers = list()

        if locations:
            for position, location_data in locations.items():
                # TODO: TO WORK ONLY WITH MAIN BASE FOR NOW:
                townhall = self.bot.townhalls.by_tag(list(townhall_tags)[0])
                if townhall.position == position:
                    new_mining_manager = MiningManager(
                        bot=self.bot,
                        position=position,
                        raw_data=location_data,
                        mineral_tags=location_data["mineral_tags"],
                        vespene_tags=location_data["vespene_tags"]
                    )
                    self.mining_managers.append(new_mining_manager)

        owned_exps = set(
            (loc, th.tag) for loc, th in self.bot.owned_expansions.items()
        )

        for exp in owned_exps:
            exp_loc, exp_th = exp
            exp_distances = list()
            free_mining_mgrs = [
                mgr for mgr
                in self.mining_managers
                if mgr.townhall == None
            ]
            for mining_mgr in free_mining_mgrs:
                distance = self.bot.distance_math_hypot(
                    exp_loc, mining_mgr.position
                )
                exp_distances.append({"dist": distance, "mgr": mining_mgr})
            closest_mm = min(exp_distances, key=lambda x: x["dist"])
            closest_mm["mgr"].set_townhall(exp_th)

        for mining_mgr in self.mining_managers:
            if not worker_tags:
                break
            if mining_mgr.townhall:
                required_workers = mining_mgr.required_workers_total
                if not required_workers >= len(worker_tags):
                    popped_workers = {
                        worker_tags.pop() for _ in range(required_workers)
                    }
                else:
                    popped_workers = worker_tags
                    worker_tags = set()
                mining_mgr.set_workers(popped_workers)

        self.unused_workers = worker_tags if worker_tags else None

    async def update(self):
        pass

    def remove_unit(self, unit):
        pass
