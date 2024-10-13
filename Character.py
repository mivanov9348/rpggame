from random import randint

class Character:
    def __init__(self, name, level = 1, health = 100, attack_power = 0, defense = 50, coins=100,weapon = None):
        self.name = name
        self.level = level
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.coins = coins
        self.weapon = weapon
        self.enemy_killed = 0

    @staticmethod
    def create_character(character_name):
        attack = randint(51, 101)
        defense = randint(51, 101)
        return Character(name=character_name, level=1, health=100, attack_power=attack, defense=defense, coins=100)

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def perform_attack(self,enemy):
        if self.weapon:
            character_attack = self.attack_power + self.weapon.damage
        else:
            character_attack = self.attack_power
            enemy.health -= character_attack
        if enemy.health <= 0:
            enemy.health = 0
            print(f'{enemy.race} has been slain!')
        else:
            print(f'{enemy.race} has {enemy.health} health left!')

    def collect_coins(self,amount):
        self.coins+=amount
        print(f'{self.name} collected {amount} coins! Total coins: {self.coins}')

    def __str__(self):
        if self.weapon:  # Check if weapon is equipped
            weapon_info = f'{self.weapon.name} ({self.weapon.damage})'
        else:
            weapon_info = 'No weapon equipped'  # Default message if no weapon

        return f'Name: {self.name}, Attack: {self.attack_power}, Health: {self.health}, Defense: {self.defense}, Coins: {self.coins}, Weapon: {weapon_info}'