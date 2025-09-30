sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
px, py = map(int, input().split())
if sx == ex:
    if px == sx and (sy < py < ey or ey < py < sy):
        print(2)
    else:
        print(0)
elif sy == ey:
    if py == sy and (sx < px < ex or ex < px < sx):
        print(2)
    else:
        print(0)
else:
    print(1)
