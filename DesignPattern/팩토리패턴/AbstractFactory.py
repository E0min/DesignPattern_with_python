from abc import *
#(abstract) Product
class Keyboard(metaclass=ABCMeta):
    @abstractmethod
    def type_words(self):
        pass

class Mouse(metaclass=ABCMeta):
    @abstractmethod
    def click_left(self):
        pass

#concreteProduct
class K380(Keyboard):
    def type_words(self):
        print("k380 키보드로 타이핑중입니다.")

class MagicKeyboard(Keyboard):
    def type_words(self):
        print("매직키보드로 타이핑중입니다. ")

class G102(Mouse):
    def click_left(self):
        print("G102마우스 좌클릭")

class MagicMouse(Mouse):
    def click_left(self):
        print("MagicMouse로 마우스 좌클릭")

#(abstract)Factory
class ComputerFactory(metaclass=ABCMeta):
    @abstractmethod
    def createKeyboard(self):
        pass

    @abstractmethod
    def createMouse(self):
        pass

#concreteFactory

class LogiComputer(ComputerFactory):
    def createMouse(self):
        return G102()

    def createKeyboard(self):
        return K380()


class AppleComputer(ComputerFactory):
    def createMouse(self):
        return MagicMouse()

    def createKeyboard(self):
        return MagicKeyboard()

class Client():
    def use(self, company):
        #product를 생산할 factory 생성
        if company =='logi':
            factory = LogiComputer()
        elif company =='apple':
            factory = AppleComputer()
        else:
            return

        #product 생산 (객체 생성)
        keyboard = factory.createKeyboard()
        mouse = factory.createMouse()

        #생산된 product를 사용
        keyboard.type_words()
        mouse.click_left()

client = Client()
client.use('logi')
client.use('apple')