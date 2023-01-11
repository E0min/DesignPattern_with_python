from abc import *

# Command
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

# Concrete Command
class SimpleCommand(Command):

    def __init__(self, payload):
        self._payload = payload

    def execute(self):
        print(f"SimpleCommand:  ({self._payload})")

# Concrete Command

class ComplexCommand(Command):

    def __init__(self, receiver, a, b) :
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self):
        print(f"ComplexCommand : do something : {self._a , self._b}")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)

class Receiver:

    def do_something(self, a):
        print(f"\nReceiver: Working on ({a}.)")

    def do_something_else(self, b) :
        print(f"\nReceiver: Also working on ({b}.)")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command):
        self._on_start = command

    def set_on_finish(self, command):
        self._on_finish = command

    def do_something_important(self):
        print("Invoker: : on_start ")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: on_finish ")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()

invoker = Invoker()
invoker.set_on_start(SimpleCommand("Say Hi!"))
receiver = Receiver()
invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Save report"))
invoker.do_something_important()