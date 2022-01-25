try:
    num1=int(input("Enter 1st number"))
    num2=int(input("Enter 2nd number"))
    result=num1/num2
    print(result)
except(ValueError,ZeroDivisionError):
    print("You have enter incorrect input")
finally:
    print("Thanks !!!")


