class Fight:
    def __init__(self):
        pass

    def fight_arena(self, character, enemy):
        is_end = False
        print(f"{character.name} vs {enemy.race}")

        while not is_end:
            print('character shte atakuva')
            character.perform_attack(enemy)
            is_end = self.check_anyone_is_killed(character, enemy)
            if is_end:  # If enemy dies, exit loop
                break
            # Then enemy attacks
            print('enemy shte atakuva')
            enemy.perform_attack(character)
            is_end = self.check_anyone_is_killed(character, enemy)

    @staticmethod
    def check_anyone_is_killed(character,enemy):
        if character.health <= 0:
            print(f'{character.name} has been killed!')
            return True
        elif enemy.health <= 0:
            print(f'{enemy.name} has been killed!')
            return True
        return False