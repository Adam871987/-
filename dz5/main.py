from lesson_2.character import Character
from Samurai import Samurai

player1 = Samurai('chel', health=100, damage=1)
player2 = Character('chely', health=50, damage=2)

print(player1)
print(player2)

if player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    print(player2)
    player2.attack(player1)
    player1.attack(player2)
    print(player2)
    player2.attack(player1)
    print(player2)
    player1.attack(player2)
    print(player2)
    player1.attack(player2)
    print(player2)
    player1.attack(player2)
    print(player2)
    player1.attack(player2)
    print(player2)
    player1.attack(player2)




print(player1)
print(player2)
