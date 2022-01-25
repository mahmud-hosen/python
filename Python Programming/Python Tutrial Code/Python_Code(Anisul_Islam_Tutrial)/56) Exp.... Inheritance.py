class Shape:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

class Triangle(Shape):
    def area(self):
        area=0.5*self.num1*self.num2
        print("Triange Area = ",area)

class Rectangle(Shape):
    def area(self):
        area=self.num1*self.num2
        print("Rectangler Area = ",area)

t=Triangle(10,20)
t.area()
r=Rectangle(20,10)
r.area()