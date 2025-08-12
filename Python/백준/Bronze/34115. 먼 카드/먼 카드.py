n = int(input())
a = list(map(int, input().split()))
b = list(reversed(a))

ans = 0
for i in range(1, n+1):
    v = a.index(i)
    w = 2 * n - 1 - b.index(i)
    ans = max(ans, w-v-1)

print(ans)
