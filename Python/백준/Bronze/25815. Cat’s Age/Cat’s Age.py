y, m = map(int, input().split())
a = 0
if y < 1:
    a = 15 * m
elif y < 2:
    a = 15 * 12 + m * 9
else:
    a = 24 * 12 + (y-2) * 48 + m * 4
print(a // 12, a % 12)
