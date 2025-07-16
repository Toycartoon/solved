sa, sb, sc = 0, 0, 0
for t in range(int(input())):
    a, b, c = map(int, input().split())
    sa += a
    sb += b
    sc += c

    mn = min(sa, sb, sc)
    if mn < 30:
        print("NO")
    else:
        print(mn)
        sa -= mn
        sb -= mn
        sc -= mn
