from bot.wrappers.units.attack_units.attack_unit import AttackUnit


class MeleeAttackUnit(AttackUnit):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
