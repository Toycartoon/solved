w = {}
s = 0
ans = 0
for i in range(int(input())):
    v = input()
    if v in w:
        if w[v] > s-w[v]:
            ans += 1
        w[v] += 1
    else:
        w[v] = 1
    s += 1
print(ans)
