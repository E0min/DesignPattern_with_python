from abc import *

#Product
class Mouse(metaclass=ABCMeta): # 추상 클래스 선언
    @abstractmethod
    def click_left(self):
        pass

    @abstractmethod
    def click_right(self):
        pass

#concreteProduct #추상클래스를 상속받는 G102, MagicMouse 클래스, 추상클래스의 추상메소드를 모두 오버라이딩 하고 있다.
class G102(Mouse):
    def click_left(self):
        print("click left by logi")

    def click_right(self):
        print("click right by logi")

class MagicMouse2(Mouse):
    def click_left(self):
        print("click left by apple")

    def click_right(self):
        print("click right by apple")

#Factory
class MouseFactory(metaclass=ABCMeta): #MouseFactory 추상클래스
    @abstractmethod
    def createMouse(self):
        pass

#concreateFactory #MouseFactory 추상클래스를 상속받는 LogiMouseFactory,AppleMouseFactory 두 클래스
class LogiMouseFactory(MouseFactory):
    def createMouse(self):
        return G102() # G102 반환

class AppleMouseFactory(MouseFactory):
    def createMouse(self):
        return MagicMouse2() #MagicMouse2 반환

#Client
class Client():
    def use(self, company):

    #사용자 요구에 따라, product를 생산할 factory 생성
        if company == 'logi':
            factory = LogiMouseFactory()
        elif company == 'apple':
            factory = AppleMouseFactory()
        else:
            return

        mymouse = factory.createMouse()
        mymouse.click_left()
        mymouse.click_right()

Client1 = Client()
C1Mouse = input("logi 아니면 apple?")
Client1.use(C1Mouse)