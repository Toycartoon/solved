import sys

input = sys.stdin.readline

a = [False for _ in range(10001)]
for t in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, y):
        a[i] = True
print(a.count(True))
