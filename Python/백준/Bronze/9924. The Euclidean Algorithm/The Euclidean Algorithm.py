a, b = map(int, input().split())

ans = 0
while a != b and b > 0:
    a, b = max(a, b) - min(a, b), min(a, b)
    ans += 1

print(ans)
