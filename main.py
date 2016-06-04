import string
from state import State
# A different subclass for each state:

class Critical(State):
    def run(self):
        print("Critical: please seek help inmediatly")

    def next(self, answer):
        return None

class NoHelp(State):
    def run(self):
        print("NoHelp: sorry, we can't help you with this")

    def next(self, answer):
        return None

class Initial(State):
    def run(self):
        return raw_input("Initial: How are you feeling today?")

    def next(self, answer):
        if 'critical' in answer:
            return Sara['critial']
        if 'lonely' in answer:
            return Sara['lonely']
        return Sara['nohelp']

class Lonely(State):
    def run(self):
        print("Lonely: so sorry to hear that")

    def next(self, answer):
        return None


# Static variable initialization:
Sara = {
    'critial': Critical(),
    'nohelp': NoHelp(),
    'initial': Initial(),
    'lonely': Lonely(),
}
currentState = Sara['initial']

while True:
    if currentState:
        answer = currentState.run()
        currentState = currentState.next(answer)
    else:
        print 'Done!'
        break



