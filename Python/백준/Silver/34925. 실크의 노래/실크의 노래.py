h, s = map(int, input().split())
if h == 1 or h == 2:
    print((h+1) // 2)
elif h == 3 or h == 4:
    print((h + 2 * s + 1) // 2)
else:
    print((h + 3 * s + 1) // 2)
