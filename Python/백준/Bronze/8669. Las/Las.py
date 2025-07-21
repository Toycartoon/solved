import sys

input = sys.stdin.readline

s = set()
for i in range(int(input())):
    g, r = map(int, input().split())
    s.add(r)

print(len(s))
