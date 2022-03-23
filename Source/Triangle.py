from GeometricObject import GeometricObject
import math

class Triangle (GeometricObject) :
    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        super().__init__(self)

    def getside1(self):
        return self.side1
    def getside2(self):
        return self.side2
    def getside3(self):
        return self.side3

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s-self.side3))
    def getPermeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return "변 1=" + str(self.side1) + "변 2 =" +str(self.side2) + "변 3 =" +str(self.side3)
    
