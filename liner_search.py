import random

data = []
for i in range(30):
    data.append(random.randint(1, 100))
print(data)
son = int(input("Sonni kiriting: "))
count = 0
for j in data:
    count += 1
    if j == son:
        print(son)
        break
print(f"Urunishalr soni: {count}")
