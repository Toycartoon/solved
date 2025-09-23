a = list(map(int, input().split()))
b = list(map(int, input().split()))

sa, sb = 0, 0
lw = -1
for i in range(10):
    if a[i] > b[i]:
        sa += 3
        lw = "A"
    elif a[i] < b[i]:
        sb += 3
        lw = "B"
    else:
        sa += 1
        sb += 1

print(sa, sb)
if sa > sb:
    print("A")
elif sa < sb:
    print("B")
else:
    if sa == sb == 10:
        print("D")
    else:
        print(lw)
