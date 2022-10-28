import time
from abc import *

#Subject
class Image(metaclass=ABCMeta):
    def __init__(self):
        self.filename = None

    @abstractmethod
    def display(self):
        pass

#RealSubject
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk() # 객체 생성시 파일 로드해온다.

    def load_from_disk(self):
        print(f'loading: {self.filename}')
        time.sleep(5)

    def display(self):
        print(f'displaying: {self.filename}')

#Proxy
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None: #real_image가 None일 경우
            self.real_image = RealImage(self.filename) #RealImage객체 생성
        self.real_image.display()

proxy_image = ProxyImage('hello.jpg') #real이 아닌 proxy로 접근
proxy_image.display()

'''프록시 패턴
1. 어떤 객체를 사용할 때 객체를 직접적으로 참조하는 것이 아닌 해당 객체를 대리하는 객체를 통해서 대상 객체에 접근하는 방식
2. 객체를 직접적으로 참조하는 것이 아닌 해당 객체를 대항하는 객체를 통해 대상 객체에 접근하는 방식을 사용하면
   해당 객체가 메모리에 존재하지 않아도 기본적인 정보를 참조하거나 설정할 수 있고, 실제 객체의 기능이 필요한 시점까지 객체의 생성을 미룰 수 있다.
3. 종류
    a. 가상 프록시
    b. 원격 프록시
    c. 보호 프록시
'''