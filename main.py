import sys
from collections import defaultdict
from random import choice
from importlib import reload, invalidate_caches

from loguru import logger as LOG

import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer

from bot import bot


colors = [
    "blue", "cyan", "green", "magenta", "red", "yellow",
    "light-blue", "light-cyan", "light-green", "light-magenta",
    "light-red", "light-yellow"
]

module_colors = defaultdict(lambda: choice(colors))

level_colors = {
    "TRACE": "white",
    "DEBUG": "magenta",
    "INFO": "green",
    "SUCCESS": "blue",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "red",
}


def formatter(record):
    module_color = module_colors[record["name"]]
    level_color = level_colors[record["level"].name]
    return "<" + module_color + ">[{time:HH:mm:ss.SSS}][{name}]</><" + \
        level_color + ">[{level}]</> <bold>{message}</>\n{exception}"


logger_filter = {
    "": False,  # By default, disable all
    "bot": "DEBUG",
    "sc2": "INFO",
    "my_module.child": "WARNING",
}


LOG.remove()
LOG.add(sys.stdout, format=formatter, filter=logger_filter, level="DEBUG")


def main():
    player_config = [
        Bot(Race.Terran, bot.Bot()),
        Computer(Race.Terran, Difficulty.VeryHard)
    ]

    gen = sc2.main._host_game_iter(
        sc2.maps.get("CatalystLE_NOAI"),
        player_config,
        realtime=False,
        save_replay_as="replays/replay.SC2Replay"
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
