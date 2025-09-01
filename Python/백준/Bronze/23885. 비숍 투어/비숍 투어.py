n, m = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())

if (n > 1 and m > 1 and (abs(ex-sx)+abs(ey-sy)) % 2 == 0) or (n == m == 1) or (sx == ex and sy == ey):
    print("YES")
else:
    print("NO")
