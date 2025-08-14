import sys

input = sys.stdin.readline

for t in range(int(input())):
    a, b, c = map(int, input().split())
    p, q = 0, 0

    if c % 2 == 0:
        p += (c // 2) * 3
        q += (c // 2) * 3
    else:
        p += (c // 2 + 1) * 3
        q += (c // 2) * 3

    if p == q:
        p += b
        q += b
    else:
        if b >= 1:
            q += 2
            b -= 1

        if b % 2 == 0:
            p += b
            q += b
        else:
            p += b-1
            q += b-1

            if p <= q:
                p += 2
            else:
                q += 2

    if max(p, q) - min(p, q) <= a:
        if p <= q:
            a -= q - p
            p = q
        else:
            a -= p - q
            q = p

        if a % 2 == 0:
            p += a // 2
            q += a // 2
        else:
            p += a // 2 + 1
            q += a // 2
    else:
        if p < q:
            p += a
        else:
            q += a

    print(max(p, q))
