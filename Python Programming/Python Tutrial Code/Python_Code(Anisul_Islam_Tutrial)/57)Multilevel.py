class A:
    def display1(self):
        print(" I am in A class ")

class B(A):
    def display2(self):
        print(" I am in B class ")

class C(B):
    def display3(self):
        super().display1()
        super().display2()

        print(" I am in C class ")


ob=C()
ob.display3()