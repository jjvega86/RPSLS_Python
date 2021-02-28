from gesture import Rock, Paper, Scissors, Lizard, Spock


class Player:
    def __init__(self, name):
        self.gestures = (Rock(), Paper(), Scissors(), Lizard(), Spock())
        self.current_score = 0
        self.name = ''

    def choose_gesture(self):
        pass

    def print_gesture_options(self):
        for gesture in self.gestures:
            index = self.gestures.index(gesture)
            print("Type " + str(index) + " and ENTER for " + gesture.name)
