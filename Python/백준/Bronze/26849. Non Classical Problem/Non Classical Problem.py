import sys

input = sys.stdin.readline

l = []
for i in range(int(input())):
    a, b = map(int, input().split())
    l.append(a / b)

print(min(l), max(l), sum(l))
