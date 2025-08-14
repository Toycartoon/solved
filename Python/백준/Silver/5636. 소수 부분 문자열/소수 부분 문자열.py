import sys

input = sys.stdin.readline

g = [i for i in range(100001)]
g[1] = 0
for i in range(2, int(len(g) ** 0.5) + 1):
    if g[i] == 0:
        continue
    for j in range(i * i, len(g), i):
        g[j] = 0

while True:
    n = input().strip()
    if n == "0":
        break

    ans = 0
    for i in range(min(5, len(n)), 0, -1):
        for j in range(i, len(n)):
            if g[int(n[j-i:j])] != 0:
                ans = max(ans, g[int(n[j-i:j])])

    print(ans)
