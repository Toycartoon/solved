ans = 0
for i in range(int(input())):
    x, y = map(int, input().split())
    d = (x ** 2 + y ** 2) ** 0.5

    if d <= 10:
        ans += 10
    elif d <= 30:
        ans += 9
    elif d <= 50:
        ans += 8
    elif d <= 70:
        ans += 7
    elif d <= 90:
        ans += 6
    elif d <= 110:
        ans += 5
    elif d <= 130:
        ans += 4
    elif d <= 150:
        ans += 3
    elif d <= 170:
        ans += 2
    elif d <= 190:
        ans += 1
print(ans)
