import random
weapons = ("Sword", "Axe", "Bow", "Dagger", "Spear", "Mace", "Crossbow", "Warhammer", "Halberd", "Flail", "Katana", "Longsword", "Rapier", "Scimitar", "Greatsword", "Trident", "Morningstar", "Throwing knife", "Whip", "Shortsword")

class Weapon:
    def __init__(self, name, damage):
        self.name=name
        self.damage = damage

    @staticmethod
    def get_weapon():
        name = random.choice(weapons)
        damage = random.randint(6,101)
        return Weapon(name,damage)

    def __str__(self):
        return f'{self.name} ({self.damage} damage)'