class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

#__str__
    def __str__(self):
        return f"({self.x},{self.y})"

#__eq__
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

#__gt__
    def __gt__(self,other):
        return self.x > other.x and self.y > other.y

#__add__
    def __add__(self, other):
        return f"({self.x + other.x},{self.y + other.y})"


    def draw(self):
        print(f"Point ({self.x},{self.y})")


point = Point(1,2)
other = Point(1,2)
print(point == other)
print(point > other)
print(point + other)