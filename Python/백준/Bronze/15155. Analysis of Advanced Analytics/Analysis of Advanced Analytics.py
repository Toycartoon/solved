n, k = map(int, input().split())
a = list(map(int, input().split()))

s = 0
ans = 1
for i in a:
    if s + i > k:
        ans += 1
        s = i
    else:
        s += i
print(ans)
