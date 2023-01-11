from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class TurnOnCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.turn_on()

class TurnOffCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.turn_off()

class LightReceiver:
    def turn_on(self):
        print('turn on')

    def turn_off(self):
        print('turn off')

class ControllerInvoke:
    def __init__(self, turn_on, turn_off):
        self._turn_on = turn_on
        self._turn_off = turn_off

    def turn_on(self):
        self._turn_on.execute()

    def turn_off(self):
        self._turn_off.execute()

light_receiver = LightReceiver()
turn_on_command = TurnOnCommand(light_receiver)
turn_off_command = TurnOffCommand(light_receiver)

controller_invoke = ControllerInvoke(turn_on_command, turn_off_command)

controller_invoke.turn_on()
controller_invoke.turn_off()