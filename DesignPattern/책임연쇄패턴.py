from abc import *

class Handler(metaclass=ABCMeta):
    @abstractmethod
    def set_next(self,handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass

class AbstractHandler(Handler):
    _next_handle= None

    def set_next(self,handler):
        self._next_handle = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handle:###########
            return self._next_handle.handle(request)####
        return None######

class MonkeyHandler(AbstractHandler):
    def handle(self, request):
        if request=="banana":
            return f'Monkey eat {request}'
        else:
            return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request):
        if request=="Meat":
            return f'Dog eat {request}'
        else:
            return super().handle(request)

class RabbitHandler(AbstractHandler):
    def handle(self, request):
        if request=="carrot":
            return f'Rabbit eat {request}'
        else:
            return super().handle(request)

monkey = MonkeyHandler()
dog = DogHandler()
rabbit = RabbitHandler()

monkey.set_next(dog).set_next(rabbit)
# monkey - dog - rabbit

print(monkey.handle('Meat'))