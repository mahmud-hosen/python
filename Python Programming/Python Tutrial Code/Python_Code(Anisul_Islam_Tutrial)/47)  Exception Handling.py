try:
    list=[10,0,30]
    resut=list[0]/list[1]
    print(resut)
    print("Done")
except ZeroDivisionError:
    print("Diviting by zero not possible ")
except IndentationError:
    print("Index Error ")

print("Sucessful")