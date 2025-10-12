x, y, p1, p2 = map(int, input().split())
for i in range(1000):
    for j in range(1000):
        if p1 + x * i == p2 + y * j:
            print(p1 + x * i)
            exit()
print(-1)
