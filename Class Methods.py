class Point:

    def __init__(self):
        self.x = 0
        self.y = 0

    @classmethod
    def one(cls):               
        return cls()

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point.one()
point.draw()