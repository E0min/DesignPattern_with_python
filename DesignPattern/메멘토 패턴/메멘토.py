class Memento:
    def __init__(self, state):
        self._state = state

    @property
    def state(self):
        return self._state

class Originator:
    def __init__(self):
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    def create_memento(self):
        return Memento(self.state)

    def get_memento_state(self, memento):
        self._state = memento.state

class CareTaker(list):
    pass

originator = Originator()
care_taker = CareTaker()

originator.state = "State #1"
originator.state = "State #2"
care_taker.append(originator.create_memento())
originator.state = "State #3"
care_taker.append(originator.create_memento())
originator.state = "State #4"

print(f"Current State: {originator.state}")
originator.get_memento_state(care_taker[0])
print(f"First saved State: {originator.state}")
originator.get_memento_state(care_taker[1])
print(f"Second saved State: {originator.state}")

# Current State: State #4
# First saved State: State #2
# Second saved State: State #3