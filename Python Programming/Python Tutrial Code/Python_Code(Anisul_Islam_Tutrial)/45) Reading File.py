file=open("mahmud.txt","r")
print(file.readable())

print(file.writable())

text=file.read()
print(text)

print(len(text))

m = file.readlines()[0]
print(m)

for line in file:
    print(line)

file.close()






