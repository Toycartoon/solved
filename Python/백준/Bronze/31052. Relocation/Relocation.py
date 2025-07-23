import sys

input = sys.stdin.readline

n, q = map(int, input().split())
x = list(map(int, input().split()))
for i in range(q):
    c, a, b = map(int, input().split())

    if c == 1:
        x[a-1] = b
    elif c == 2:
        print(abs(x[a-1]-x[b-1]))
