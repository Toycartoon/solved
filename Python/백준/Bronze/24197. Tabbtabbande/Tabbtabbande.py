n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
now = 1
for i in a:
    ans += min((n+i-now) % n, (n-i+now) % n)
    now = i
print(ans)
