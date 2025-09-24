mnx, mxx, mny, mxy = 101, 0, 101, 0
for i in range(int(input())):
    x, y = map(int, input().split(","))
    mnx = min(x-1, mnx)
    mny = min(y-1, mny)
    mxx = max(x+1, mxx)
    mxy = max(y+1, mxy)
print(f"{mnx},{mny}\n{mxx},{mxy}")
