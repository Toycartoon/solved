n = int(input())
h = list(map(int, input().split()))

h.sort()
ans = 0
for i in range(n):
    ans += (h[i] * pow(2, i, 10 ** 9 + 7)) % (10 ** 9 + 7)

print(ans % (10 ** 9 + 7))
