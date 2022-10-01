class Singleton():
    def __new__(cls): #__new__는 항상 cls를 인자로 하며 __new는 Object의 메소드가 아닌 클래스의 메소드로 오버라이딩된 new이다.
        if not hasattr(cls, 'instance'): # 해당 클래스가 instance라는 이름을 가진 속성이 없으므로 조건문 시작
            print("make instance") # 인스턴스 생성
            cls.instance = super().__new__(cls) # Object클래스(부모)에 저장되어있는 __new__객체를 불러왔다.
        return cls.instance

s1 = Singleton()
print("Object created", s1)

s2 = Singleton()
print("Object created", s2)

"""
- hasattr(object,name) -> 해당 Object에 name 가지면 True를 반환
"""