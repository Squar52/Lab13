import math
class PointSpace:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def SetCoord(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def DisplayCoord(self):
        print(f"({self.x}, {self.y}, {self.z})")
    def Octant(self):
        "Номер октанти 1-8; 0, якщо точка лежить на координатній площині чи осі."
        if self.x == 0 or self.y == 0 or self.z == 0:
            return 0
        if self.z > 0:
            if self.x > 0:
                return 1 if self.y > 0 else 4
            return 2 if self.y > 0 else 3
        if self.x > 0:
            return 5 if self.y > 0 else 8
        return 6 if self.y > 0 else 7

    def Dist(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)