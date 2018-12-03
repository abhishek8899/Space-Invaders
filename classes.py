class freeze():
    def __init__(self, x, y, ti):
        self.x = x
        self.y = y
        self.t = ti


class fire():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class fire1(fire):
    def __init__(self, x, y):
        fire.__init__(self, x, y)


class fire2(fire):
    def __init__(self, x, y):
        fire.__init__(self, x, y)
