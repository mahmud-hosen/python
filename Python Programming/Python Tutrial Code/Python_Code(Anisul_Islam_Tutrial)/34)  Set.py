num2=set([10,20,30,40])
num =  {10,20,30,40}
num3 = {10,20,50,60}
print(num2)
num2.add(9)
print(num2)
num2.remove(9)
print(num2)
print(4 in num2)
print( 4 not in num2)

print(num | num3) # Common and Uncommon value but not double
print(num & num3) # Common  value
print(num-num3)   # Subtract  num3 from num

