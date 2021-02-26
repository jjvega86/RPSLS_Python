class Player:
    def __init__(self):
        self.name = ''
        self.gestures = ("rock", "paper", "scissors", "lizard", "spock")
        self.chosen_gesture = ''

    def choose_gesture(self):
        return self.chosen_gesture

    def print_gesture_options(self):
        for gesture in self.gestures:
            print(gesture)
