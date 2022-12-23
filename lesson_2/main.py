from character import Character

player1 = Character('chel', damage=2)
player2 = Character('chely', health=50)
print(player1)
print(player2)

player1.attack(player2)

while (player1.alive == True and player2.alive == True):
 player1.attack(player2)
 player2.attack(player1)
 player1.is_alive()
 player2.is_alive()
 print(player1)
 print(player2)
else:
    print('противник пал')
