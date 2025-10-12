n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort()
ans = float('inf')
for i in range(n//2):
    ans = min(ans, a[i]+a[-i-1])
print(ans)
