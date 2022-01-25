import re
pattern =r"[aeiou]"
if re.match(pattern,"mahmud"):
    print("Match")

# Different


pattern1 =r"[0-9][A-Z][a-z]"
if re.match(pattern1,"0As"):
    print("Match")