from abc import *

class Soccer(metaclass=ABCMeta):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

class SoccerPlayer(Soccer):
    def attack(self):
        print("축구선수 공격능력")

    def defend(self):
        print("축구선수 수비능력")

class BaseballAdapter(Soccer):       ########
    def __init__(self, Baseball):    ########
        self.Baseball = Baseball     ########

    def attack(self):
        self.Baseball.hit()

    def defend(self):
        self.Baseball.defend()

class Baseball:
    def hit(self):
        print("공을 타격하는 능력")

    def defend(self):
        print("야구선수가 수비하는 능력")


BTC = BaseballAdapter(Baseball())
BTC.attack()
BTC.defend()