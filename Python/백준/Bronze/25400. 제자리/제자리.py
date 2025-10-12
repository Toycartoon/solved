n = int(input())
a = list(map(int, input().split()))

idx = 1
ans = 0
for i in a:
    if i != idx:
        ans += 1
    else:
        idx += 1
print(ans)
