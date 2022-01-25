# . $
import re
pattern=r"colo..r$"
if re.match(pattern,"colouar"):
    print("Match")
# *

pattern2=r"(ab)*"
if re.match(pattern2,"colour"):
    print("Match")

# +

pattern3=r"ice(-)?cream"
if re.match(pattern3,"icecream"):
    print("Match3")


# { }

pattern4=r"a{1,3}$"
if re.match(pattern4,"aaa"):
    print("Match4")

