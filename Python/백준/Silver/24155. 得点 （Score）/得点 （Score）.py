import sys

input = sys.stdin.readline

a = []
for i in range(int(input())):
    a.append(int(input()))

v = sorted(a, reverse=True)
for i in a:
    print(v.index(i)+1)
