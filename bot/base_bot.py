import sc2

from bot.managers.base_manager import BaseManager
from bot.wrappers.base_wrapper import BaseWrapper
from bot.wrappers import Wrappers


class BaseBot(sc2.BotAI):
    # managers = list()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.raw_affects_selection = True
        Wrappers.set_bot_instance(self)

    async def update(self):
        await BaseWrapper.update_subclasses()
        await BaseManager.update_subclasses()

    async def get_expansions(self, locations):
        location_dict = dict()
        for position, location_data in locations.items():
            location_dict[position] = {
                "mineral_tags": location_data.mineral_field.tags,
                "vespene_tags": location_data.vespene_geyser.tags
            }

        return location_dict

    async def chat(self, message):
        await self.client.chat_send(message, False)

    def get_xyz(self, point):
        if isinstance(point, sc2.position.Point3):
            x, y, z = point
        elif isinstance(point, sc2.position.Point2):
            x, y, z = (*point, self.get_terrain_z_height(point))
        else:
            raise NotImplementedError("get_xyz not implemented for this type")

        return (x, y, z)

    def draw_sphere(self, position, radius=1, color=None):
        x, y, z = self.get_xyz(position)
        position = sc2.position.Point3((x, y, z))
        color = (255, 255, 255) if not color else color

        self.client.debug_sphere_out(
            p=position,
            r=radius,
            color=color
        )

    def draw_text(self, text, position, color=None, size=12):
        x, y, z = self.get_xyz(position)
        position = sc2.position.Point3((x, y, z))
        color = (255, 255, 255) if not color else color

        self.client.debug_text_world(
            text=text,
            pos=position,
            color=color,
            size=size
        )

    def draw_text_info(self, entries, position, x_offset=2.5):
        x, y, z = self.get_xyz(position)

        range_offset = int(x_offset * 10)

        for y_offset, entry in zip(
            range(range_offset, -range_offset, -5),
            entries
        ):
            y_offset /= 10

            text_position = sc2.position.Point3((
                x + x_offset,
                y + y_offset,
                z
            ))
            self.draw_text(entry, text_position)
