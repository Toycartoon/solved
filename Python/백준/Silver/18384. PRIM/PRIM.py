import sys

input = sys.stdin.readline

g = [i for i in range(1000000)]
g[1] = 0
for i in range(2, int(len(g) ** 0.5) + 1):
    if g[i] == 0:
        continue

    for j in range(i * i, len(g), i):
        g[j] = 0

for t in range(int(input())):
    l = list(map(int, input().split()))
    ans = 0
    for i in l:
        for x in range(i, len(g)):
            if g[x] != 0:
                ans += x
                break

    print(ans)
