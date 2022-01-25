import  re
# Match
pattern=r"col"
if re.match(pattern,"colour is a colour , I love colour "):
    print(" Match ")
else:
    print("Not Match")

#Search

if re.search(pattern,"colour is a colour , I love colour "):
    print(" Found ")
else:
    print("Not Found")
#Findall
print(re.findall(pattern,"Red is a colour , I love red colour "))