class Point:

    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self):
        print(f"Point ({self.x},{self.y})")

point = Point()
point.draw()