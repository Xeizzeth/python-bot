from bot.wrappers.base_wrapper import BaseWrapper


class Worker(BaseWrapper):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
