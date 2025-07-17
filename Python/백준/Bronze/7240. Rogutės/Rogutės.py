n, s = map(int, input().split())
ans = 0

for i in range(n):
    if ans > s:
        ans -= 1
    ans += int(input())

print(ans)
