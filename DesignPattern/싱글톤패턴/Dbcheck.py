class Dbcheck:
    _instance = None
    def __new__(cls): # 객체를 한번만 메모리에 할당하는 __new__
        if not Dbcheck._instance:
            Dbcheck._instance = super().__new__(cls)
        return Dbcheck._instance

    def __init__(self):
        self._servers=[]

    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")

hc1 = Dbcheck()
hc2 = Dbcheck()

print(hc1) #한 번만 생성된 객체
print(hc2) #한 번만 생성된 객체

hc1.addServer() # addServer메소드를 통해 _servers에 Server1~4까지 추가
print(hc1._servers)

print("Schedule DB Check for servers (1)...")
for i in range(4):
    print("Checking ", hc1._servers[i])

hc2.changeServer() #hc1과 hc2는 같은 객체를 공유하므로 h2에서 changeServer을 실행하더라도 상태를 공유하기때문에 hc1의 Server1~4에서 change가 일어난다.
for i in range(4):
    print("Checking ", hc2._servers[i])
