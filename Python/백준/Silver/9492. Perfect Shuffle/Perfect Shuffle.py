while True:
    n = int(input())
    if n == 0:
        break

    a = []
    for i in range(n):
        a.append(input())

    u, d = a[:(n+1)//2], a[(n+1)//2:]
    for i in range(len(u)):
        print(u[i])
        if i < len(d):
            print(d[i])
