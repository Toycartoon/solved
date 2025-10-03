from math import ceil

v, n = map(int, input().split())
for i in range(10, 100, 10):
    print(((n * v) * i + 99) // 100, end=" ")
