import random
races = ('Orc','Elf','Zombie','Skeleton', 'Dwarf', 'Troll','Goblin','Dwarves','Elves','Giants','Ghouls')

class Enemy:
    def __init__(self,race, health, attack):
        self.race = race
        self.health = health
        self.attack = attack

    def generate_enemy():
        race = random.choice(races)
        health = random.randint(21,101)
        attack = random.randint(11,41)
        return Enemy(race,health,attack)

    def enemy_attack(self, player):
        enemy_attack = random.randint(1, self.attack)
        print(f'The {self.attack} attacks with {self.attack}!')
        player.health-=enemy_attack
        if player.health <=0:
            player.health=0
            print(f'{player.name} are dead!')

    def __str__(self):
        return f'{self.race} - Health: {self.health}, Attack: {self.attack}'
