n = int(input())
a = list(map(int, input().split()))

ans = float('inf')
for i in range(1, n):
    ans = min(ans, abs(a[i]-a[i-1]))
print(ans)
