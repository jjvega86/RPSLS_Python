from gesture import Gesture


class Scissors(Gesture):
    def __init__(self):
        self.name = 'scissors'
        self.loses_to = {'rock', 'spock'}
