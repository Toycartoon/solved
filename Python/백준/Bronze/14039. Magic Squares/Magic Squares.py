g = [list(map(int, input().split())) for _ in range(4)]
s = sum(g[0])

f = True
for i in range(4):
    if sum(g[i]) != s:
        f = False
        break

for i in range(4):
    if sum(list(zip(*g))[i]) != s:
        f = False
        break

if f:
    print("magic")
else:
    print("not magic")
