book= []
book.append("Java ")
book.append("Python")
book.append("HTML")
print(book)

book.pop()
print("Top Book is ",book[-1])


book.pop()
print("Top Book is ",book[-1])

book.pop()

if not book:
    print("Empty")


