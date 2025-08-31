import sys

input = sys.stdin.readline

s = input().strip()
l, r = 0, len(s)
for i in range(int(input())):
    a, b = map(int, input().split())
    l += a
    r = min(r, l+b)

print(s[l:r])
