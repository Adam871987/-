import random
from Person import person
from Person import action


human1 = person('Sasha')
human2 = person('Danya')
human3 = person('Petya')
work = action(name = 'работать', money = 10, mood = -10, health = -5)
rest = action(name = 'отдыхать', money = -10, mood = 15, health = 5)



while True:
    humans = [human1, human2, human3]
    actions = [work, rest]
    try:
        print(1)
        print(len(humans))
        human1.do(random.choice(actions))
    except:
        humans.remove(human1)
    try:
        human2.do(random.choice(actions))
        print(2)
    except:
        humans.remove(human2)
    try:
        human3.do(random.choice(actions))
        print(3)
    except:
        humans.remove(human3)


    if len(humans) == 0:
        print('Все люди yмерли')
        break