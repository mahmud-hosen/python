from abc import ABC,abstractclassmethod
class Shape(ABC):
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2


        @abstractclassmethod
        def area(self):
            pass


class Triangle(Shape):
    def area(self):
        area=0.5*self.num1*self.num2
        print("Triangle Area = ",area)

class Rectangle(Shape):
    def area(self):
        area=self.num2*self.num1
        print("Rectangle Area = ",area)


r=Rectangle(10,20)
r.area()

t=Triangle(10,20)
t.area()