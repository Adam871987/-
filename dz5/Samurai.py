from lesson_2.character import Character


class Samurai(Character):
    max_health = 100
    factor = 0

    def __init__(self, name, health=100, damage=1, defence=0, factor=0):
        Character.__init__(self, name, health, damage, defence)
        self.max_health = self.health
        self.factor = factor

    def attack(self, target):
        factordamage = self.damage + (self.damage * self.factor)
        target.take_damage(factordamage)
        self.factor += 0.1
        if self.factor > 0.5 :
          self.factor = 0