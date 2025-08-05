n = int(input())

ans = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        if i ** 2 == n:
            ans += 1
        else:
            ans += 2

print(ans)
