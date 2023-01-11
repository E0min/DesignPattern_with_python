from abc import *

class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("state A")

class ConcreteStateB(State):
    def handle(self):
        print("state B")

class Context:
    def __init__(self):
        self.state = None

    def setState(self,state):
        self.state = state

    def getState(self,state):
        return self.state

    def request(self):##
        self.state.handle()##

context = Context()
stateA = ConcreteStateA()
stateB = ConcreteStateB()

context.setState(stateA)
context.request()