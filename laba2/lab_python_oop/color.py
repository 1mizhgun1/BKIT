class Color:
    def __init__(self):
        self.param = None

    @property
    def parametr(self):
        return self.param

    @parametr.setter
    def parametr(self, param):
        self.param = param