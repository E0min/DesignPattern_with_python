from abc import *
# Product
class Animal(metaclass = ABCMeta): # 추상 클래스 선언
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):

    def do_say(self):
        print("왈 왈")

class Cat(Animal):
    def do_say(self):
        print("야옹 야옹!!")

class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say() # eval(object_type)()두번째 빈 괄호는 입력받는 objecy_type 클래스 생성자의 매개변수가 위치할 자리이다.

ff = ForestFactory()
animal = input("Dog or Cat") # animal에는 Dog또는 Cat문자열이 저장된다.
ff.make_sound(animal) # animal은 object_type인자로 받아진다.

"""
eval 함수
"""