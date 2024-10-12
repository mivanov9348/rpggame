from random import randint

class Character:
    def __init__(self, name, level = 1, health = 100, attack = 0, defense = 50, coins=100,weapon = None):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense
        self.coins = coins
        self.weapon = weapon

    def create_character(name):
        attack = randint(51, 101)
        defense = randint(51, 101)
        return Character(name=name, level=1, health=100, attack=attack, defense=defense, coins=100)

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self,enemy):
        character_attack = self.attack + self.weapon.damage
        enemy.health -= character_attack
        if enemy.health<=0:
            enemy.health = 0
            print(f'{enemy.name} has slain!')
        else:
            print(f'{enemy.name} has {enemy.health} left!')

    def collect_coins(self,amount):
        self.coins+=amount
        print(f'{self.name} collected {amount} coins! Total coins: {self.coins}')

    def __str__(self):
        if self.weapon:  # Check if weapon is equipped
            weapon_info = f'{self.weapon.name} ({self.weapon.damage})'
        else:
            weapon_info = 'No weapon equipped'  # Default message if no weapon

        return f'Name: {self.name}, Attack: {self.attack}, Health: {self.health}, Defense: {self.defense}, Coins: {self.coins}, Weapon: {weapon_info}'