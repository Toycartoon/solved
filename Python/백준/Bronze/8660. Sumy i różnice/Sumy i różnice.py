n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    if i < 0:
        ans += n-1
print(ans)
