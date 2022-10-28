from abc import *

class Color(metaclass=ABCMeta):
    ##구현
    @abstractmethod
    def fill_color(self):
        pass

class RedColor(Color):
    def fill_color(self):
        print("빨간색으로 채워!")

class BlueColor(Color):
    def fill_color(self):
        print("파란색으로 채워!")

class Shape(metaclass=ABCMeta):
    ##기능
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def color_it(self):
        pass

class Rectangle(Shape):
    def __init__(self,color):
        super().__init__(color) #Shape 클래스의 생성자에 넣는 인자값

    def color_it(self):
        print("사각형 선택!")
        self.color.fill_color() # color로 Color를 상속받는 객체가 인자로 전달되고 구현이 실행된다.


class Circle(Shape):
    def __init__(self, color):
        super().__init__(color)

    def color_it(self):
        print("원 선택!")
        self.color.fill_color()

blue_rectangle = Rectangle(BlueColor())
blue_rectangle.color_it()

'''
브릿지 패턴
- 기능과 구현을 분리하여 두가지가 독립적으로 변할 수 있게 한다.
'''