a, b = map(int, input().split())
g = [[*input()] for _ in range(a)]

f = False
for i in range(a):
    s = set()
    for j in range(a):
        if i == j:
            continue
        s.update({*g[j]})

    if len(s) <= 1:
        f = True
        break

g = list(zip(*g))
for i in range(b):
    s = set()
    for j in range(b):
        if i == j:
            continue
        s.update({*g[j]})

    if len(s) <= 1:
        f = True
        break

if f:
    print("Yes")
else:
    print("No")
