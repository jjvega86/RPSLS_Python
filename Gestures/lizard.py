from gesture import Gesture


class Lizard(Gesture):
    def __init__(self):
        self.name = 'lizard'
        self.loses_to = {'rock', 'scissors'}
