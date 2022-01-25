n=int(input("Enter the end number "))

sum=0
for x in range(1,n+1,1) :             # 1+2+3+4+......n
    sum=sum+x
    print(x)
print(sum)

print("#2+4+6+......n")
for x in range(2,n+1,2) :              #2+4+6+......n
    sum=sum+x
    print(x)
print("Sum : ", sum)



for x in range(1,n+1,1) :              #  Square
    sum=sum+x
    print(x*x)
print("Sum : ", sum)



