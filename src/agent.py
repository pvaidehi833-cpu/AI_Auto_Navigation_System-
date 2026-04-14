class Agent:
    def __init__(self, path):
        self.path = path
        self.index = 0

    def move(self):
        if self.index < len(self.path):
            pos = self.path[self.index]
            self.index += 1
            return pos
        return None