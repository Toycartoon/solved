import sys

input = sys.stdin.readline

g = [i for i in range(100001)]
g[1] = 0
for i in range(2, int(len(g) ** 0.5) + 1):
    if g[i] == 0:
        continue
    for j in range(i * i, len(g), i):
        g[j] = 0


s = sorted(list(set(g)))[1:]
for t in range(int(input())):
    w = {}
    n = int(input())

    idx = len(s)-1
    while n > 1 and idx >= 0:
        if n % s[idx] == 0:
            x = 0
            while n % s[idx] == 0:
                x += 1
                n //= s[idx]
            w[s[idx]] = x
        idx -= 1

    for i in sorted(w.items()):
        print(*i)
