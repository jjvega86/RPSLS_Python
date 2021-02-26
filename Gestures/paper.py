from gesture import Gesture


class Paper(Gesture):
    def __init__(self):
        self.name = 'paper'
        self.loses_to = {'scissors', 'lizard'}
