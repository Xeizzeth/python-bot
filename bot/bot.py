from .base_bot import BaseBot

class Bot(BaseBot):
    async def on_before_start(self):
        pass

    async def on_start(self):
        print("i very well")

    async def on_step(self, iteration: int):
        if iteration == 0:
            for worker in self.workers:
                worker.attack(self.enemy_start_locations[0])
