import sys

input = sys.stdin.readline

p = []
e = []
for i in range(int(input())):
    a, b = input().split()
    if a == "pig":
        p.append(int(b))
    else:
        e.append(int(b))

x = max(p)
ans = x
for i in e:
    if i < x:
        ans += i

print(ans)
