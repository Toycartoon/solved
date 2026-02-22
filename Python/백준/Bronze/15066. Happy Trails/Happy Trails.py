from math import sin

ans = 0
for i in range(int(input())):
    a, d = map(int, input().split())
    ans += d * sin(a * 0.0174533)
print(f"{ans:.02f}")
