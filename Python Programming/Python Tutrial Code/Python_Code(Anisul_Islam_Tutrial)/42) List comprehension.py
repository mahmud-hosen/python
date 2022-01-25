num=[1,2,3,4,5]
result=[x*x for x in num]
print(result)

# Filtering use by Comprehensions :
res=[x for x in num if x%2==0]
print(res)