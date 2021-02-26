from gesture import Rock, Paper, Scissors, Lizard, Spock


class Player:
    def __init__(self):
        self.name = ''
        self.gestures = (Rock(), Paper(), Scissors(), Lizard(), Spock())
        self.chosen_gesture = ''

    def choose_gesture(self):
        return self.chosen_gesture

    def print_gesture_options(self):
        for gesture in self.gestures:
            index = self.gestures.index(gesture)
            print("Type" + index + "and ENTER for" + gesture.name)
