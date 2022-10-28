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

class ForestFactory(object): #입력된 객체명을 생성하는 팩토리
    def make_sound(self, object_type):
        return eval(object_type)().do_say() # eval(object_type)()두번째 빈 괄호는 입력받는 object_type 클래스 생성자의 매개변수가 위치할 자리이다.

ff = ForestFactory()
animal = input("Dog or Cat") # animal에는 Dog또는 Cat문자열이 저장된다.
ff.make_sound(animal) # animal은 object_type인자로 받아진다.

"""
eval()
animal은 object_type인자로 받아진다. 여기서 특이한 메소드를 볼 수 있는데 이는 eval()메소드이다. animal은 분명 문자열로 받아졌을 텐데 신기하게 알아서 
animal에 받아진 문자열이 클래스 타입이란 것을 잘 알아먹었다. 그래서 원래 문자열 인자를 받고 문자열과 동일한 클래스 타입이 있다면 클래스 타입으로 반환하는 메소드인가
찾아봤더니 이 용도로 쓰이는 메소드는 아니라고 했다. eval() 메소드는 인자로 받은 식을 문자열로 실행하는 메소드라고 설명이 되어있다. 그러니깐 eval() 메소드의 인자 값의 
타입은 반드시 문자열이어야 한다. 
"""