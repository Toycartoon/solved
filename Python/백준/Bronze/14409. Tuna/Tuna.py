n = int(input())
x = int(input())

ans = 0
for i in range(n):
    p1, p2 = map(int, input().split())
    if abs(p1-p2) <= x:
        ans += max(p1, p2)
    else:
        ans += int(input())
print(ans)
