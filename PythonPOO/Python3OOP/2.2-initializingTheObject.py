class Point:

    def __init__(self, x, y):
        self.move(x, y)
    
    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

point = Point(3, 5)
print(point.x, point.y)

