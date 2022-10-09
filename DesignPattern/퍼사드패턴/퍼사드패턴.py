class wash:
    def __init__(self):
        print("보일러 켜기")

    def bathroom(self):
        print("샤워 혹은 머리감기")


class cloth:
    def __init__(self):
        print("옷입기")

    def wearing(self):
        print("옷 다입었습니다.")

class BeforeOut:
    def __init__(self):
        pass

    def turnoff(self):
        print("보일러 끄기")

class GetOut(): # 퍼사드 클래스:

    def __init__(self):
        print("외출준비 프로세스")

    def arrange(self):
        self.ws = wash()
        self.ws.bathroom()
        self.cl = cloth()
        self.cl.wearing()
        self.bo = BeforeOut()
        self.bo.turnoff()

class Me(): # 클라이언트
    def __init__(self):
        print("친구만나러 나가야겠다.")

    def preparetoout(self): #복잡한 내부 구현대신 퍼사드 클래스를 통해 쉬운 실행 가능하게 만든다.
        GO =GetOut()
        GO.arrange()


I = Me()
I.preparetoout()