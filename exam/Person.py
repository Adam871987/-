class Nohealth(Exception):
    def __init__(self, message='у вас закончилось здоровье. Вы умерли'):
        Exception.__init__(self, message)

class Nomood(Exception):
    def __init__(self, message='у вас закончилось настроение. Вам очень грустно'):
        Exception.__init__(self, message)

class Nomoney(Exception):
    def __init__(self, message='у вас закончились деньги. Вы банкрот'):
        Exception.__init__(self, message)

class action:
    name = ''
    health = 100
    mood = 100
    money = 0

    def __init__(self, name='', health=100, mood=1, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

class person:
    name = ''
    health = 100
    mood = 100
    money = 100

    def __init__(self, name='', health=100, mood=100, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return f'{self.name} ' \
               f'(health:{self.health},' \
               f' mood:{self.mood},' \
               f' money: {self.money})'

    def change_state(self, health, mood, money):
        self.health += health
        self.mood += mood
        self.money += money
        if self.health < 0:
            raise Nohealth
            pass
        if self.mood < 0:
            raise Nomood
            pass
        if self.money < 0:
            raise Nomoney
            pass

    def do(self, action):
        self.health += action.health
        self.mood += action.mood
        self.money += action.money
        if self.health < 0:
            raise Nohealth
            pass
        if self.mood < 0:
            raise Nomood
            pass
        if self.money < 0:
            raise Nomoney
            pass
