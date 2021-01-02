from collections import defaultdict

from loguru import logger as log

from sc2.ids.unit_typeid import UnitTypeId

from .base_manager import BaseManager

from bot.wrappers import (
   Mineral, Vespene,
   CommandCenter,
   Scv,
   Wrappers
)

from random import randint

class MiningManager(BaseManager):
    def __init__(
        self,
        bot,
        position,
        raw_data,
        townhall_tag=None,
        mineral_tags=None,
        vespene_tags=None,
        worker_tags=None,
    ):
        super().__init__()

        self.randint = randint(0, 100000)

        self.bot = bot

        self.position = position
        self.raw_data = raw_data

        self.townhall_tag = townhall_tag if townhall_tag else None
        self.set_townhall(townhall_tag)

        self.mineral_tags = mineral_tags if mineral_tags else set()
        self.vespene_tags = vespene_tags if vespene_tags else set()

        self.worker_tags = worker_tags if worker_tags else set()

        self.minerals = dict()
        self.vespenes = dict()

        self.mineral_workers = dict()
        self.vespene_workers = dict()
        self.undistributed_workers = dict()

        for mineral_tag in self.mineral_tags:
            self.minerals[mineral_tag] = Mineral(tag=mineral_tag)

        for vespene_tag in self.vespene_tags:
            self.vespenes[vespene_tag] = Vespene(tag=vespene_tag)

        self.recalculate_workers()

    def set_townhall(self, townhall_tag):
        if townhall_tag:
            townhall_unit_unwrapped = self.bot.townhalls.by_tag(townhall_tag)
            if townhall_unit_unwrapped.type_id in (
                UnitTypeId.COMMANDCENTER,
                UnitTypeId.PLANETARYFORTRESS,
                UnitTypeId.ORBITALCOMMAND,
                UnitTypeId.COMMANDCENTERFLYING,
                UnitTypeId.ORBITALCOMMANDFLYING
            ):
                self.townhall = CommandCenter(tag=townhall_tag)
        else:
            self.townhall = None

    def set_workers(self, worker_tags):
        for worker_tag in worker_tags:
            worker_unit_unwrapped = self.bot.workers.by_tag(worker_tag)
            if worker_unit_unwrapped.type_id == UnitTypeId.SCV:
                self.undistributed_workers[worker_tag] = Scv(tag=worker_tag)
            # TODO: Add other worker types

        self.recalculate_workers()

    def recalculate_workers(self):
        self.required_workers_total = (
            (len(self.minerals) * 2)
            # TODO: Commented until I start working with vespene
            # + (len(self.vespenes) * 3)
        )

        self.required_mineral_workers_total = (
            len(self.minerals) * 2
        )

        self.required_vespene_workers_total = (
            len(self.vespenes) * 3
        )

        self.undistributed_workers = {
            **self.mineral_workers,
            **self.vespene_workers,
            **self.undistributed_workers
        }

        self.mineral_workers = dict()
        self.vespene_workers = dict()

        self.needed_workers = (
            self.required_workers_total
            - len(self.undistributed_workers)
        )

    def remove_unit(self, unit):
        if unit.type_id == UnitTypeId.MINERALFIELD:
            if unit.tag in self.minerals:
                self.update_minerals()
        elif unit.type_id == UnitTypeId.VESPENEGEYSER:
            if unit.tag in self.vespenes:
                self.update_vespenes()
        self.recalculate_workers()

    def update_minerals(self):
        location_info = self.bot.expansion_locations_dict[self.position]
        location_mineral_tags = location_info.mineral_field.tags

        new_mineral_tags = location_mineral_tags - self.mineral_tags
        destroyed_mineral_tags = self.mineral_tags - location_mineral_tags

        self.mineral_tags = location_mineral_tags

        for mineral_tag in destroyed_mineral_tags:
            log.debug(
                f"Removing {mineral_tag} "
                + f"position: {self.minerals[mineral_tag].position} "
                + "from MINERALS"
            )
            self.minerals.pop(mineral_tag)

        for mineral_tag in new_mineral_tags:
            self.minerals[mineral_tag] = Mineral(tag=mineral_tag)

            log.debug(
                f"Added {mineral_tag} "
                + f"position: {self.minerals[mineral_tag].position} "
                + "to MINERALS"
            )

    def update_vespenes(self):
        location_info = self.bot.expansion_locations_dict[self.position]
        location_vespene_tags = location_info.vespene_geyser.tags

        new_vespene_tags = location_vespene_tags - self.vespene_tags
        destroyed_vespene_tags = self.vespene_tags - location_vespene_tags

        self.vespene_tags = location_vespene_tags

        for vespene_tag in destroyed_vespene_tags:
            log.debug(
                f"Removing {vespene_tag} "
                + f"position: {self.vespenes[vespene_tag].position} "
                + "from VESPENES"
            )

            self.vespenes.pop(vespene_tag)

        for vespene_tag in new_vespene_tags:
            self.vespenes[vespene_tag] = Vespene(tag=vespene_tag)

            log.debug(
                f"Added {vespene_tag} "
                + f"position: {self.vespenes[vespene_tag].position} "
                + "to VESPENES"
            )

    async def update(self):
        await self.draw_debug_info()

    async def draw_debug_info(self):
        entries = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten"
        ]

        # DRAWING INFO NEXT TO POSITION RELATED TO MINING MANAGER
        self.bot.draw_sphere(self.position, 2.5)
        self.bot.draw_text_info(entries, self.position)

        for mineral in self.minerals.values():
            amount = mineral.minerals_left
            workers = 0

            mineral_entries = (
                f"minerals: {amount}",
                f"workers: {workers}"
            )

            self.bot.draw_sphere(
                mineral.position,
                color=(0, 255, 255)
            )

            self.bot.draw_text_info(
                entries=mineral_entries,
                position=mineral.position,
                x_offset=0.5
            )

        for vespene in self.vespenes.values():
            amount = vespene.vespene_left
            workers = 0

            vespene_entries = (
                f"vespene: {amount}",
                f"workers: {workers}"
            )

            self.bot.draw_sphere(
                vespene.position,
                radius=1.5,
                color=(0, 255, 0)
            )
            self.bot.draw_text_info(
                entries=vespene_entries,
                position=vespene.position,
                x_offset=1.5
            )
