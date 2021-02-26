from gesture import Gesture


class Spock(Gesture):
    def __init__(self):
        self.name = 'spock'
        self.loses_to = {'lizard', 'paper'}
