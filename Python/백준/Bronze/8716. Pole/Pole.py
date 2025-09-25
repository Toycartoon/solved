mnx, mxy, mxx, mny = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
if mxx < x3 or x4 < mnx or mxy < y4 or y3 < mny:
    print(0)
    exit()

mnx = max(mnx, x3)
mxy = min(mxy, y3)
mxx = min(mxx, x4)
mny = max(mny, y4)
print((mxy-mny) * (mxx-mnx))
