from collections import defaultdict

from loguru import logger as LOG

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

        self.update_tags()

        super().__init__()

    def update_tags(self):
        for tag in self.mineral_tags:
            mineral = self.bot.mineral_field.by_tag(tag)
            if mineral.is_visible:
                self.minerals[tag] = mineral

        for tag in self.vespene_tags:
            vespene = self.bot.vespene_geyser.by_tag(tag)
            if vespene.is_visible:
                self.vespenes[tag] = vespene

    async def update(self):
        self.update_tags()
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
            amount = mineral.mineral_contents
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
            amount = vespene.vespene_contents
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
