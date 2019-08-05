import random

class Dice(object):
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.choice(range(1, self.sides+1))


class Character(object):
    def __init__(self, health = 10, strength = 5, damage = 2, armor = 5):
        self.health = health
        self.strength = strength
        self.damage = damage
        self.armor = armor
        self.character_state = 'Alive'

    def __str__(self):
        return f"I'm game character and my strength is {self.strength}"

    def attack(self, target_character):
        target_character.defend(self.damage)
        print(f"This is method from {self.__class__.__name__}")

    def defend(self, damage):       # jezeli nasza postac sie broni, to chcemy rzucc kostka. jezeli wyrzucimy wiecej nic 3 punkty, to nic nam sie nie dzieje. jak mniej, to bierze strzal
        dice_to_defend = Dice().roll()          # zainicjowanie obiektu Dice() - musi byc pusty nawias!!! i od razu uzycie roll() - mozna by rozbic na dwie osobne czesci
        if dice_to_defend > 3:
            return

        damage_to_health = max(damage - self.armor, 0)      # tutaj obliczamy, ile bedzie damage'u dla zdrowia, czyli po uwzglednieniu armoru (czyli jak damage jest mniejszy niz armor, to armor przyjmuje caly damage i zdrowie nic nie traci - bedzie 0)
        self.armor = max(self.armor - damage, 0)       # inny zapis: self.armor -= damage
        self.health = max(self.health - damage_to_health, 0)

        if self.health == 0:
            print("DEATH!")
            self.character_state = 'Dead'


class Barbarian(Character):
    def __init__(self, anger = 1):
        super().__init__()
        self.anger = anger

    def attack(self, target_character):
        print(f"This is method from {self.__class__.__name__}")
        target_character.defend(self.damage + self.anger)



########################################################################################################################

# game=Dice()
#
# print(f"Rolled with number: {game.roll()}")