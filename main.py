from importlib import reload, invalidate_caches

import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer

from bot import bot


def main():
    player_config = [
        Bot(Race.Terran, bot.Bot()),
        Computer(Race.Terran, Difficulty.VeryHard)
    ]

    gen = sc2.main._host_game_iter(
        sc2.maps.get("CatalystLE_NOAI"),
        player_config,
        realtime=False
    )

    next(gen)
    while True:
        if input('Press enter to reload or type "q" to exit: ') == 'q':
            exit()

        reload(bot)
        player_config[0].ai = bot.Bot()
        gen.send(player_config)


if __name__ == "__main__":
    main()
