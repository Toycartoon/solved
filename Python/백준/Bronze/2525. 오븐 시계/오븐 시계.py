a, b = map(int, input().split())
c = int(input())

h = a
m = b + c
if m >= 60:
    h += m // 60
    m = m % 60
if h >= 24:
    h = 0 + h % 24

print(h, m)