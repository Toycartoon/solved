import sys

input = sys.stdin.readline

s = input().strip()
c = s[0]
s = {*s}
for i in range(int(input())):
    x = input().strip()
    if len({*x} - s) == 0 and len(x) >= 4 and c in x:
        print(x)
