import sys

input = sys.stdin.readline

a = []
n, m = map(int, input().split())
for i in range(n):
    filename, extension = input().strip().split(".")
    a.append((filename, extension))

s = set()
for i in range(m):
    s.add(input().strip())

a.sort(key=lambda x: (x[0], int(x[1] not in s), x[1]))
for i in a:
    print(".".join(i))
