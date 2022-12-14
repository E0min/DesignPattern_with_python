from abc import *

class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):

    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self ## 외우기

        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            print(sender)
            self._component2.do_d()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()

# Colleague
class BaseComponent:

    def __init__(self, mediator = None):
        self.mediator = mediator

    @property
    def mediator(self): #게터
        return self._mediator

    @mediator.setter
    def mediator(self, mediator): #세터
        self._mediator = mediator

# concrete Colleague
class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 은 do_a 를 수행한다.")
        self.mediator.notify(self, "A")

    def do_b(self):
        print("Component 1 은 do_b 를 수행한다.")
        self.mediator.notify(self, "B")

# concrete Colleague
class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 는 do_c 를 수행한다.")
        self.mediator.notify(self, "C")

    def do_d(self):
        print("Component 2 는 do_d 를 수행한다.")
        self.mediator.notify(self, "D")

c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)
print("C1 operation A.")
c1.do_a()