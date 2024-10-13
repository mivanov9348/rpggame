import random

races = ('Orc','Elf','Zombie','Skeleton', 'Dwarf', 'Troll','Goblin','Dwarves','Elves','Giants','Ghouls')

class Enemy:
    def __init__(self,):
        self.race = random.choice(races)
        self.health = random.randint(21,101)
        self.attack_power = random.randint(11,41)

    def perform_attack(self, character):
        print(f'{self.race} attack!')
        enemy_attack = random.randint(1, self.attack_power)
        print(f'The {self.attack_power} attacks with {self.attack_power}!')
        character.health-=enemy_attack
        if character.health <=0:
            character.health=0
            print(f'{character.name} are dead!')

