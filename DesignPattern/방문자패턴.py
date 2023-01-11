from abc import *

class Component(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteComponentA(Component):
  def accept(self, visitor):
    visitor.visit_concrete_component_a(self) ## self 넘기는거 기억하기
    #visitor 가 가지고 있는 visit 함수 호출

  def method_of_concrete_component_a(self):
    return "A"

class ConcreteComponentB(Component):
  def accept(self, visitor):
    visitor.visit_concrete_component_b(self)
    #visitor 가 가지고 있는 visit 함수 호출

  def method_of_concrete_component_b(self):
    return "B"

class Visitor(metaclass=ABCMeta):
  @abstractmethod
  def visit_concrete_component_a(self, concrete_component_a):
    pass
    # concrete_component_a 를 방문했을 때, 처리할 로직, 메서드 visit()
    # 하위 클래스에서 구현한다.

  @abstractmethod
  def visit_concrete_component_b(self, concrete_component_b):
    pass
    # concrete_component_b 를 방문했을 때, 처리할 로직, 메서드 visit()
    # 하위 클래스에서 구현한다.

class ConcreteVisitor1(Visitor):
  def visit_concrete_component_a(self, component): ##기억하기
    print(f"{component.method_of_concrete_component_a()} + ConcreteVisitor1")

  def visit_concrete_component_b(self, component):
    print("{} + ConcreteVisitor1".format(component.method_of_concrete_component_b()))


class ConcreteVisitor2(Visitor):
  def visit_concrete_component_a(self, component):
    print(f"{component.method_of_concrete_component_a()} + ConcreteVisitor2")

  def visit_concrete_component_b(self, component):
    print("{} + ConcreteVisitor2".format(component.method_of_concrete_component_b()))


components = [ConcreteComponentA(), ConcreteComponentB()] #방문객체가 방문할 공간

visitor1 = ConcreteVisitor1() #방문객체
for component in components:
  component.accept(visitor1) #방문할공간에 방문객체가 방문

visitor2 = ConcreteVisitor2()
for component in components:
  component.accept(visitor2)