t, p = map(int, input().split())
v = list(map(int, input().replace("X", "0").split()))

ans = 0
for i in range(t-1):
    a = list(map(int, input().replace("X", "0").split()))
    if a.count(0) < v.count(0) or (a.count(0) == v.count(0) and sum(a) <= sum(v)):
        ans += 1
print(ans)
