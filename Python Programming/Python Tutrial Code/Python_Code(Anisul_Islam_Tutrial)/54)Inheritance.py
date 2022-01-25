class Phone:
    def call(self):
        print("Plz Call")
    def message(self):
        print("Plz Message")

class Samsung(Phone):
    def photo(self):
        print("Take a photo")

s=Samsung()
s.call()
s.message()
s.photo()
print(issubclass(Samsung,Phone))