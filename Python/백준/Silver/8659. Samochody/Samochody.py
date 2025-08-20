n = int(input())
s = list(map(int, input().split()))

v = sum(s)
ans = 0
for i in s:
    if i == 0:
        ans += v
    else:
        v -= 1

print(ans)
