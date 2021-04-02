from typing import List


class Hero:
    hp = 100
    power = 10
    magic_hp = 200
    speed = 1
    tools = []

    def fight(self,hero:'Hero'):
        while True:
            hero.hp -= self.power
            if hero.hp <=0:
                return True
            self.hp -= hero.power
            if self.hp <= 0:
                return False
    def winner(self,hero1,hero2):
        if hero1.hp <= 0:
            return False
        if hero2.hp <=0:
            return True

    def fight_many(self,hs:List["Hero"]):
        pass
