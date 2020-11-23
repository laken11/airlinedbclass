class MenuItem:
    name: str
    action = None

    def __init__(self, name, action):
        self.name = name
        self.action = action

    def invoke(self):
        self.action()
