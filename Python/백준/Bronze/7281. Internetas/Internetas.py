n = int(input())
t, x = map(int, input().split())

ans = t
b = t
for i in range(n-1):
    t, x = map(int, input().split())

    if x == 1:
        ans = max(ans, t-b)
        b = t

print(ans)
