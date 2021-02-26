class Gesture:
    def __init__(self):
        self.name = ''
        self.loses_to = {}


class Lizard(Gesture):
    def __init__(self):
        self.name = 'lizard'
        self.loses_to = {'rock', 'scissors'}


class Paper(Gesture):
    def __init__(self):
        self.name = 'paper'
        self.loses_to = {'scissors', 'lizard'}


class Rock(Gesture):
    def __init__(self):
        self.name = 'rock'
        self.loses_to = {'paper', 'spock'}


class Scissors(Gesture):
    def __init__(self):
        self.name = 'scissors'
        self.loses_to = {'rock', 'spock'}


class Spock(Gesture):
    def __init__(self):
        self.name = 'spock'
        self.loses_to = {'lizard', 'paper'}
