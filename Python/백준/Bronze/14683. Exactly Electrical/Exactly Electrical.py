a, b = map(int, input().split())
c, d = map(int, input().split())
t = int(input())

v = abs(a - c) + abs(b - d)
if v > t or v % 2 != t % 2:
    print("N")
else:
    print("Y")
