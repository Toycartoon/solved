n = int(input())
a = sorted(list(map(int, input().split())))

s = sum(a)
ans = 0
for i in range(n // 2):
    s -= (a[i] + a[-i-1])
    ans += (a[i] + a[-i-1]) * s + a[i] * a[-i-1]

print(ans)
