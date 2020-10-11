from collections import defaultdict

from loguru import logger as LOG

from sc2.ids.unit_typeid import UnitTypeId

from .base_manager import BaseManager

from bot.wrappers import (
   Mineral, Vespene
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

        self.mineral_tags = mineral_tags if mineral_tags else set()
        self.vespene_tags = vespene_tags if vespene_tags else set()

        self.worker_tags = worker_tags if worker_tags else set()

        self.minerals = dict()
        self.vespenes = dict()

        self.mineral_workers = dict()
        self.vespene_workers = dict()
        self.undistributed_workers = dict()

        for mineral_tag in self.mineral_tags:
            self.minerals[mineral_tag] = Mineral(tag=mineral_tag, bot=self.bot)

        for vespene_tag in self.vespene_tags:
            self.vespenes[vespene_tag] = Vespene(tag=vespene_tag, bot=self.bot)

    def remove_unit(self, unit):
        if unit.id == UnitTypeId.MINERALFIELD:
            if unit.tag in self.minerals:
                LOG.info(f"Removing {unit.tag} from MINERALS")
                self.minerals.pop(unit.tag)
        elif unit.id == UnitTypeId.VESPENEGEYSER:
            if unit.tag in self.vespenes:
                LOG.info(f"Removing {unit.tag} from VESPENES")
                self.vespenes.pop(unit.tag)

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
