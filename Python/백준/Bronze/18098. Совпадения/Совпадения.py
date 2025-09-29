import sys

input = sys.stdin.readline

s = set()
n = int(input())
for i in range(n):
    a = int(input())
    s.add(a)
print(n-len({*range(1, n+1)}-s))
