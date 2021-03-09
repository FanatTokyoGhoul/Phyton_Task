class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def __repr__(self):
        return f"{self.x1} {self.x2} {self.x3}"

    def get_area(self):
        return 0.5 * abs((self.x2 - self.x1) * (self.y3 - self.y1) - (self.x3 - self.x1) * (self.y2 - self.y1))

    def sort_key(s):
        return s.get_area()