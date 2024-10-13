from Character import Character
from Room import Room

class Game():
    def __init__(self):
        pass

    def game_loop(self, character):
        while character.health>0:
            print(f'Hello {character.name}! In front of you you will see 3 doors. Choose one! ')
            print("1: Door 1")
            print("2: Door 2")
            print("3: Door 3")

            try:
                choice =  int(input('Choose a door (1,2,3)'))
                if choice in [1,2,3]:
                    room = Room()
                    room.enter(character)
                else:
                    print('Invalid Choice! Choose again')
            except ValueError:
                print("Invalid input! Choose again!")

        print(f'Game Over! {character.name} Die! Enemy killed: {character.enemy_killed}, Coins Earned: {character.coins}')


