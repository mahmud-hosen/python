word=0
letter=0
digit=0
text=input("Enter your text : ")
for x in text:
    x=x.lower()
    if x>='a' and x<='z':
        letter=letter+1

    if x>='0' and x<='9':
        digit=digit+1

    if x==' ':
        word=word+1

print(letter)
print(digit)
print(word+1)
