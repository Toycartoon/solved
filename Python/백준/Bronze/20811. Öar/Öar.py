n = int(input())
if n <= 2:
    print(n)
    exit()

n -= 2
f, g = 1, 1
idx = 3
while True:
    if idx % 2 == 1:
        f += g
        n -= f
    else:
        g += f
        n -= g

    if n <= 0:
        print(idx)
        break
    idx += 1
