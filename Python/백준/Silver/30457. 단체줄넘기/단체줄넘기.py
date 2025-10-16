n = int(input())
a = list(map(int, input().split()))
v = [0 for _ in range(1001)]
for i in a:
    v[i] += 1

ans = 0
for i in v:
    if i != 0:
        ans += min(2, i)
print(ans)
