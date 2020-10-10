import sc2

class BaseBot(sc2.BotAI):
    managers = list()

    async def update(self):
        for manager in self.managers:
            await manager.update()

    async def chat(self, message):
        await self.client.chat_send(message, False)

    def draw_sphere(self, position, radius=1):
        z = self.get_terrain_z_height(position)
        point = sc2.position.Point3((position.x, position.y, z))
        self.client.debug_sphere_out(
            p=point,
            r=radius
        )
