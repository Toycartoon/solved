n = int(input())
g = [i+1 for i in range(n)]

x = 0
while 2 ** (x + 1) <= n:
    x += 1

temp = n
for i in range(x, 0, -1):
    if g[2 ** i-1] != 2 ** i:
        continue

    d = temp - 2 ** i
    for v in range(2 ** i - d, 2 ** i + d + 1):
        g[v-1] = (2 ** i) + -(v - 2 ** i)
    temp = 2 ** i - d - 1

for i in g:
    print(i)
