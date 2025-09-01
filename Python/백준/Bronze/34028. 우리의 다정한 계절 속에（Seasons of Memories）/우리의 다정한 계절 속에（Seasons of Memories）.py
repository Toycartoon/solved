a, b, c = map(int, input().split())
ans = (a - 2015) * 4

d = b * 100 + c
if 301 <= d <= 531:
    ans += 2
elif 601 <= d <= 831:
    ans += 3
elif 901 <= d <= 1130:
    ans += 4
else:
    if d <= 229:
        ans += 1
    else:
        ans += 5

print(ans)
