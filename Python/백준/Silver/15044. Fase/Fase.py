w = {}
n = int(input())
x = int(input())
for i in range(n):
    v = int(input())
    if v in w:
        w[v] += 1
    else:
        w[v] = 1

ans = 0
for i in sorted(w.keys(), reverse=True):
    ans += w[i]
    if ans >= x:
        break

print(ans)
