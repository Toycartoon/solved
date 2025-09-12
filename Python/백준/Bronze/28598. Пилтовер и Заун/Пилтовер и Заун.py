x1, x2, n = map(int, input().split())
if n == 0:
    if x1 == x2:
        print("YES")
    else:
        print("NO")
elif x1 - x2 >= 2 * n and (x1 - x2) % 2 == 0:
    print("YES")
else:
    print("NO")
