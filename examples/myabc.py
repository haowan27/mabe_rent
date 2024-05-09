from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,w,h):
      self.w = w
      self.h = h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2*( self.w + self.h)