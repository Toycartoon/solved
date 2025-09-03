n = int(input())
k = int(input())

ans = 0
for i in range(1, n+1):
    for x in range(2, k+1):
        while True:
            if i % x == 0:
                i //= x
            else:
                break
    if i == 1:
        ans += 1
print(ans)
