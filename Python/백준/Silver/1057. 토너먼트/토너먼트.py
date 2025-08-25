n, a, b = map(int, input().split())
r = 1
while True:
    if (a+1) // 2 == (b+1) // 2:
        print(r)
        break
    else:
        a = (a+1) // 2
        b = (b+1) // 2
        r += 1
