x = int(input())
n = int(input())

ans = x
for i in range(n):
    p = int(input())
    ans += x - p

print(ans)
