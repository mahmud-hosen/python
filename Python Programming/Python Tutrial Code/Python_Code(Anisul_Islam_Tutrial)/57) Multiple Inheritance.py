class A:
    def display(self):
        print(" I am in A class ")

class B:
    def display(self):
        print(" I am in B class ")

class C(B,A):
    pass


ob=C()
ob.display()