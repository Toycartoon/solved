g = [i for i in range(100001)]
g[1] = 0

for i in range(2, int(len(g) ** 0.5) + 1):
    if g[i] == 0:
        continue

    for j in range(i * 2, len(g), i):
        g[j] = 0

n = int(input())
if g[n] != 0:
    print("Yes")
else:
    print("No")
