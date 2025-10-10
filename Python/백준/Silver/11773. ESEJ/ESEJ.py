import random

a, b = map(int, input().split())
for i in range(b):
    x = ""
    for _ in range(random.randint(1, 15)):
        x += random.choice([*"qwertyuiopasdfghjklzxcvbnm"])
    print(x, end=" ")
