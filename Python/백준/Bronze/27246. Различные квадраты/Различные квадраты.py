n = int(input())
ans = 0
k = 1
while n >= k ** 2:
    n -= k ** 2
    ans += 1
    k += 1
print(ans)
