from datetime import datetime
from string import ascii_letters
from random import sample
from abc import *


class Originator():
    _state = None

    def __init__(self, state):
        self._state = state
        print(f"Originator : My initial state is: {self._state}")

    def do_something(self): # 상태변경 메소드
        print(" doing something important ")
        self._state = self._generate_random_string(10) #상태 변경
        print(f"Originator : My state has changed to: {self._state}")

    def _generate_random_string(self, length=5):
        return "".join(sample(ascii_letters, length))

    def save(self): # 상태저장
        return ConcreteMemento(self._state) #Memento타입으로 저장

    def restore(self, memento): # 저장 상태 얻기
        self._state = memento.get_state()
        print(f"Originator : Restore My state has changed to: {self._state}")


class Memento(ABC):#저장할 자료구조
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_date(self):
        pass

class ConcreteMemento(Memento):
    def __init__(self, state):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self):
        return self._state

    def get_name(self):
        return f" {self._date} / ({self._state[0:5]}...) "

    def get_date(self):
        return self._date


class Caretaker(): #Memoto클래스를 순서대로 저장하는 클래스

    def __init__(self, originator):
        self._mementos = []
        self._originator = originator

    def backup(self):
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")#
        try:#
            self._originator.restore(memento)#
        except Exception:#
            self.undo()#

    def show_history(self):
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())

originator = Originator(" Dankook university ") # 초기상태
caretaker = Caretaker(originator)

caretaker.backup()
originator.do_something()
print()
caretaker.backup()
caretaker.show_history()

caretaker.undo()
caretaker.undo()