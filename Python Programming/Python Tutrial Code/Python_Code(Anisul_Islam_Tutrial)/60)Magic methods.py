class Bike:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def __eq__(self,other):
        return self.name==other.name and self.color==other.color
    def display(self):
        print(f"name={self.name},color={self.color}")

bike1=Bike("Yamaha R15","Blue")
bike2=Bike("Discover","Red")
bike1.display()
bike2.display()
print(bike1==bike2)
