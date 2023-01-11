from abc import *

 #Receiver
class Chef:
    def __init__(self, name):
        self.name = name

    def cook_spaghetti(self):
        print(f"{self.name}가 스파게티를 요리합니다.")
        pass

    def cook_pizza(self):
        print(f"{self.name}가 피자를 요리합니다.")
        pass
# Invoker
class Waiter:
    def __init__(self):
        self.orders = []

    def add_order(self, order): #어떠한 행위를 받기
        self.orders.append(order)

    def execute_orders(self):#어떠한 행위를 실행하게 하기
        for order in self.orders:
            order.execute()
        self.orders = []

# Commmand
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

# Concrete Command
class SpaghettiOrder(Order):
    def __init__(self, chef):
        self.chef = chef

    def execute(self):
        self.chef.cook_spaghetti()


class PizzaOrder(Order):
    def __init__(self, chef):
        self.chef = chef

    def execute(self):
        self.chef.cook_pizza()

chef = Chef("고든램지")
waiter = Waiter()

# 고객(클라이언트)는 주문서를 작성하고, 웨이터에게 건낸다.
# 쉐프 (Receiver)에게 스파게티를 요청하는 Command ( 주문 , 요청 )
order = SpaghettiOrder(chef)

waiter.add_order(order)
# 주문을 다 받은 웨이터(invoker)는 주문을 실행한다.
waiter.execute_orders()

# 고객(클라이언트)는 주문서를 작성하고, 웨이터에게 건낸다.
order = PizzaOrder(chef)  # 주방장(Receiver)에게 피자를 요청하는 주문서
waiter.add_order(order)

# 주문을 다 받은 웨이터(invoker)는 주문을 실행한다.
waiter.execute_orders()