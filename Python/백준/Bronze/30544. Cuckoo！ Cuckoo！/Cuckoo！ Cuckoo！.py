h, m = map(int, input().split(":"))
n = int(input())

while n > 0:
    if m % 15 == 0:
        if m == 0:
            n -= h
        else:
            n -= 1

    if n <= 0:
        break

    m += 1
    if m >= 60:
        h += 1
        m -= 60

    if h > 12:
        h -= 12

print(f"{str(h).zfill(2)}:{str(m).zfill(2)}")
