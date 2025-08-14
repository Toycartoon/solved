import sys

input = sys.stdin.readline

g = [i for i in range(1000000)]
g[1] = 0

for i in range(2, int(len(g) ** 0.5) + 1):
    if g[i] == 0:
        continue
    for j in range(i * i, len(g), i):
        g[j] = 0

s = []
for i in g:
    if i != 0:
        s.append(i)

n = int(input())
print(s[n-1])
