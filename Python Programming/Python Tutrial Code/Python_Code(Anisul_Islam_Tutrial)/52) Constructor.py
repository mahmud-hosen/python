class Student:
    roll=""
    gpa=""
  def _init_(self, roll, gpa):
     self.roll=roll
     self.gpa=gpa

  def display(self):
   print(f"Roll : {self.roll},Gpa {self.gpa}")

rahim=Student(101,3.75)
rahim.display()

karim=Student(102,3.99)
karim.display()

