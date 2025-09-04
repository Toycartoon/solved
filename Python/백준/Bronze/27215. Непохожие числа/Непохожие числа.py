from math import gcd

x = int(input())
l = int(input())
r = int(input())

ans = []
for i in range(l, r+1):
    if i == x:
        continue

    g = gcd(x, i)
    c = 0
    for v in range(1, g+1):
        if g % v == 0:
            c += 1

    if c <= 2:
        ans.append(i)

print(len(ans))
print(*ans)
