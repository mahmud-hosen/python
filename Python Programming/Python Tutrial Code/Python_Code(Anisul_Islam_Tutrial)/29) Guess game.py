from random import  randint
while 1:
 guessnum=int(input("Enter Your guess num : "))
 randomnum=randint(1,5)
 if guessnum==randomnum :
    print("Win ")
    break
 else:
    print("Lost ")
    print(" Random Num is : ",randomnum)