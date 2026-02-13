w = 0
s = 0
n = int(input())
for i in range(n):
    g = input()
    s += abs(ord(g[0])-69)

    if g[1] == "1" and g[0] in "ABC":
        w += 0.05
    elif g[1] == "2" and g[0] in "ABC":
        w += 0.025
print((s / n) + w)
