import random
from Enemy import Enemy
from Fight import Fight

class Room:
    def __init__(self):
        self.event = random.choice(['enemy','empty','treasure'])

    def enter(self,character):
        if self.event == 'enemy':
            enemy = Enemy()
            print(f'The room is not empty! {enemy.race} stand above you!')
            current_fight = Fight()
            current_fight.fight_arena(character,enemy)
        elif self.event == 'treasure':
            treasures = [random.randint(10, 100), random.randint(50, 150),random.randint(1, 200)]  # Dynamic treasure values
            random.shuffle(treasures)
            while True:
                try:
                    choice = int(input("Choose a box(1,2 or 3): "))
                    if choice in [1,2,3]:
                        selected_treasure = treasures[choice-1]
                        character.coins += selected_treasure
                        print(f"You opened box {choice} and found {selected_treasure} coins!")
                        print(f"Total coins: {character.coins}")
                        break
                    else:
                        print("Invalid choice. Please choose 1, 2, or 3.")
                except ValueError:
                    print("Please enter a valid number (1, 2, or 3).")
        else:
            print('The room is empty.')