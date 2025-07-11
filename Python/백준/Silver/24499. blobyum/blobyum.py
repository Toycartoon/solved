n, k = map(int, input().split())
a = list(map(int, input().split()))

a.extend(a)
v = 0
ps = [0]
for i in a:
    v += i
    ps.append(v)

ans = 0
for x in range(k, len(a)):
    ans = max(ps[x]-ps[x-k], ans)

print(ans)
