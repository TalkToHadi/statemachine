import string
from state import State
# A different subclass for each state:

class Critical(State):
    def run(self):
        print("Please seek help inmediatly")

    def next(self, answer):
        return None

class NoHelp(State):
    def run(self):
        print("Sorry, I can't help you with this")

    def next(self, answer):
        return None

class Burocrazy(State):
    def run(self):
        print("Sorry, I can't help you with this but I know who can!")
        print("You should check Burocrazy, those guys are cool")

    def next(self, answer):
        return None

class Initial(State):
    def run(self):
        print("Hi there. My name is Hadi")
        print("I'm here for you. What's up")
        print("A - I feel up")
        print("B - I feel down")
        return raw_input("")

    def next(self, answer):
        if 'up' in answer:
            return FeelUp()
        if 'down' in answer:
            #return FeelDown()
        return NoHelp()

class FeelUp(State):
    def run(self):
        print("Great!")
        return raw_input("Would you like to cheer someone up?")

    def next(self, answer):
        if 'y' in answer:
            return Introduce()
        return NoHelp()

class Lonely(State):
    def run(self):
        print("So sorry to hear that")
        return raw_input("Would you like to meet new people?")

    def next(self, answer):
        if 'yes' in answer:
            return Introduce()
        return HomeSick()

class Introduce(State):
    def run(self):
        print("Let me introduce you to my friend Hans!")

    def next(self, answer):
        return None

class Sports(State):
    def run(self):
        print("You could visit your university sports club and join a team :)")

    def next(self, answer):
        return None

class Music(State):
    def run(self):
        print("Check the bars at WurtsPlatz, there are always cool gigs there!")

    def next(self, answer):
        return None

class HomeSick(State):
    def run(self):
        print("It's hard to be away from home, but there are pleanty of\
              things you can do!")
        return raw_input("What are you into?")

    def next(self, answer):
        if 'sports' in answer:
            return Sports()
        if 'music' in answer:
            return Music()
        return NoHelp()


currentState = Initial()

while True:
    if currentState:
        answer = currentState.run()
        currentState = currentState.next(answer)
    else:
        break



