from Dzien10.game import Character, Barbarian

player = Character(20)              # domyslne wartosci: (self, health = 10, strength = 5, damage = 2, armor = 5) - podwyzszamy health do 20
enemy = Character()                 # domyslne wartosci: (self, health = 10, strength = 5, damage = 2, armor = 5)
barbarian = Barbarian()

how_many_attacks = 5

for number_of_attacks in range(how_many_attacks):
    if player.character_state == 'Dead':
        break
    enemy.attack(player)

barbarian.attack(player)


print(f"Player has armor: {player.armor} and health: {player.health}")



