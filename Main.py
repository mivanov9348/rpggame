from Character import Character
from Weapon import Weapon
from Enemy import Enemy

character_name = input(f'Welcome! What is your name?')
main_character = Character.create_character(character_name)
weapon = Weapon.get_weapon()
main_character.equip_weapon(weapon)
print(f'Hello, {main_character.name}!')
result = input(f'Write Y to generate an enemy!').lower()
if result == "y".lower():
    for i in range (30):
        enemy = Enemy.generate_enemy()
        print(f'{enemy.race} - Health: {enemy.health}, Attack: {enemy.attack}')
