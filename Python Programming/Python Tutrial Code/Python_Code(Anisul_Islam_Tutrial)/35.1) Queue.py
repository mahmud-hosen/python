from collections import  deque
bank=deque(["Anis","Karim","Bijoy"])
print(bank)

bank.popleft()
print(bank)

bank.popleft()
bank.popleft()
print(bank)

if not bank:
    print("Not person")