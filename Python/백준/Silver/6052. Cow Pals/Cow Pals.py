s = int(input())

n = s
while True:
    v = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            v += i

    u = 0
    for i in range(1, v // 2 + 1):
        if v % i == 0:
            u += i

    if u == n and u != v:
        print(u, v)
        break
    n += 1
