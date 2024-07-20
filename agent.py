import numpy as np



class Agent:
    def __init__(self, position: int, informed: bool):
        self.position = position
        self.informed = informed

    def move(self, max_position: int):
        move = np.random.choice([-1, 1])
        new_position = self.position + move
        if new_position < 0:
            new_position = 0
        elif new_position >= max_position:
            new_position = max_position - 1
        self.position = new_position

    def inform(self):
        self.informed = True