from abc import *
class Strategy(metaclass=ABCMeta):

  @abstractmethod
  def do_algorithm(self, data):
    pass

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        return reversed(sorted(data))

class Context():

  def __init__(self, strategy):
    self.__strategy = strategy

  @property
  def strategy(self):
    return self.__strategy

  @strategy.setter
  def strategy(self, strategy):
    self.__strategy = strategy


  def do_some_logic(self):
    result = self.__strategy.do_algorithm(["a", "b", "c", "d", "e"])
    print(",".join(result))

context = Context(ConcreteStrategyA())
context.do_some_logic()
context.strategy = ConcreteStrategyB()
context.do_some_logic()