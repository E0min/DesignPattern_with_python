class Monostate:
    __shared_state = {"a":13}
    def __init__(self):
        self.__dict__ = self.__shared_state  #  __dict__: 클래스의 인스턴스변수와 값을 {변수:값}형태의 딕셔너리로 가지고있음 /
        return print(self.__dict__)

b1 = Monostate() # b1과 b2는 서로 다른 객체이다.
b2 = Monostate()

b1.a = 44
#__dict__는 객체의 인스턴수변수와 값을 딕셔너리로 가지는 게 아닌, '클래스'의 인스턴스 변수와 값을 딕셔너리로 가진다 그래서 b1과 b2는 서로다른 객체이지만
#같은 __shared_data를 공유하는 것 처럼 보인다.


print("Monostate Object 'b1': ", b1) # Monostate Object 'b1':  <__main__.Monostate object at 0x104c23fd0>
print("Monostate Object 'b2': ", b2) # Monostate Object 'b2':  <__main__.Monostate object at 0x104c23f10>

print("Monostate Object 'b1': ", b1.__dict__)
print("Monostate Object 'b2': ", b2.__dict__)

"""
싱글톤 패턴에 의하면 객체는 하나만 존재해야한다. 하지만 일부 개발자들은 객체의 생성 여부보다 객체의 상태, 행위가 더 중요하다고 한다.
모노스테이트 싱글톤 패턴은 모든 객체가 같은 상태를 공유한다.
"""