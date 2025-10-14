a, b, c = map(int, input().split())
if abs(a) + abs(b) > c:
    print("NO")
    exit()

if (c - (abs(a) + abs(b))) % 2 == 0:
    print("YES")
else:
    print("NO")
