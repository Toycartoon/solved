from math import inf

n = int(input())

ans = ()
s = inf
for a in range(1, n+1):
    if n % a != 0:
        continue
    for b in range(1, (n // a)+1):
        if (n // a) % b != 0:
            continue
        c = n // a // b
        if min(s, 2 * (a * b) + 2 * (a * c) + 2 * (b * c)) != s:
            s = 2 * (a * b) + 2 * (a * c) + 2 * (b * c)
            ans = (a, b, c)

print(*ans)
