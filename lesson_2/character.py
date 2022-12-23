class Character:
    name = 'chel'
    health = 100
    damage = 1
    defence = 0
    alive = True

    def __init__(self, name='chel', health=100, damage=1, defence=0, alive = True):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
        self.alive = alive
    def __str__(self):
        return f' == {self.name} ==\n' \
            f' Здоровье : {self.health}\n' \
            f' урон : {self.damage}\n ' \
            f' Защита : {self.defence}\n'
    def take_damage(self, damage):
        self.health -= damage

    def attack(self, target):
        target.take_damage(self.damage)

    def is_alive(self):
        if self.health > 0:
            self.alive = True;
            return
        else:
            self.alive = False;






