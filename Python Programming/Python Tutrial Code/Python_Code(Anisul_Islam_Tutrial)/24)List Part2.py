list=[1,200,30,4,50]
l=len(list)              # length of list
print(l)

list.append(100)         # value add last position
print(list)
print(len(list))

list.insert(0,"hi")       # value add accouding to position
print(list)

list.remove("hi")       # remove item
print(list)

list.sort()            # list item sort , small  to big
print(list)

list.reverse()         # reverse list
print(list)

list.pop()             # remove last item from list
list.pop()
print(list)

list2=list.copy()      # List copy
print(list2)

pos=list2.index(100)    # Position
print(pos)


c=list2.count(100)       # Count
print(c)

list2.clear()
print(list)
