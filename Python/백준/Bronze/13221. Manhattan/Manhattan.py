x, y = map(int, input().split())
a = []
for t in range(int(input())):
    tx, ty = map(int, input().split())
    a.append((abs(tx-x)+abs(ty-y), tx, ty))

a.sort()
print(*a[0][1:])
