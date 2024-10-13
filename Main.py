from Character import Character
from Weapon import Weapon
from Game import Game

character_name = input(f'Welcome! What is your name?')
main_character = Character.create_character(character_name)
print(main_character)

weapon = Weapon.get_weapon()
main_character.equip_weapon(weapon)
print(f'Hello, {main_character.name}!')

game_instance = Game()
game_instance.game_loop(main_character)