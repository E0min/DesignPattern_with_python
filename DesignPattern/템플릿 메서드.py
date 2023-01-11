from abc import *

class AbstractClass(metaclass=ABCMeta):

    ## 로직의 요소
    @abstractmethod
    def _required_operations1(self):
        pass

    @abstractmethod
    def _required_operations2(self):
        pass

    ## 실제 큰 뼈대나 핵심이 되는 로직 혹은 단계
    def template_method(self):#
        self._required_operations1()#
        self._required_operations2()#


class ConcreteClass1(AbstractClass):
    def _required_operations1(self):
        print("ConcreteClass1 : Implemented Operation1")

    def _required_operations2(self):
        print("ConcreteClass1 : Implemented Operation2")

class ConcreteClass2(AbstractClass):
    def _required_operations1(self):
        print("ConcreteClass2 : Implemented Operation1")

    def _required_operations2(self):
        print("ConcreteClass2 : Implemented Operation2")

concrete_logic = ConcreteClass1()#
concrete_logic.template_method()#

concrete_logic = ConcreteClass2()
concrete_logic.template_method()