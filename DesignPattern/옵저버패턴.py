import random
from abc import *

class Subject:
    _state = 0
    _observers = []

    def attach(self, observer):##상태전달받을 객체를 추가하는 메소드
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer):##상태전달받을 삭제하는 메소드
        self._observers.remove(observer)

    def notify(self):
        print("Subject: Notifying observers")
        for observer in self._observers:
            observer.update(self) ## 2. 상태변화 보고

    def some_logic(self):
        print("Subject: do something important")
        self._state = random.randrange(0,10)
        print(f'Subject: My state has {self._state}')
        self.notify() ## 1. 상태변화 후

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self,subject):
        pass

class ConcreteObserverA(Observer):
    def update(self,subject):
        if subject._state <5:
            print("ObserverA: Reacted to the event")

class ConcreteObserverB(Observer):
    def update(self,subject):
        if subject._state >=5:
            print("ObserverB: Reacted to the event")

s = Subject() #상태 변화를 처음 알게되는 객체

ObA = ConcreteObserverA() # 상태변화를 전달 받을 객체
ObB = ConcreteObserverB() # 상태변화를 전달 받을 객체

s.attach(ObA) # 상태 변화를 알기 위해 객체 등록
s.attach(ObB) # 상태 변화를 알기 위해 객체 등록

s.some_logic()
s.some_logic()





