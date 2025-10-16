n, m, k = map(int, input().split())
a = set(input().split())
b = set(input().split())

sa, sb = 0, 0
for i in input().split():
    if i in a:
        sa += 1
    elif i in b:
        sb += 1

if sa < sb:
    print("B")
elif sa > sb:
    print("A")
else:
    print("TIE")
