g = [i for i in range(1000001)]
g[1] = 0
for i in range(2, int(len(g) ** 0.5) + 1):
    if g[i] == 0:
        continue

    for j in range(i * i, len(g), i):
        g[j] = 0

s = []
for i in range(2, len(g)):
    if g[i] != 0:
        s.append(i)

for i in range(int(input())):
    n = int(input())
    f = True
    for x in s:
        if n % x == 0:
            f = False
            break

    if f:
        print("YES")
    else:
        print("NO")
