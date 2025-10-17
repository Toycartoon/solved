for t in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n ** 2)]

    f = True
    for i in a:
        if sorted(list(set(i))) != list(range(1, n**2+1)):
            f = False
            break

    for i in zip(*a):
        if sorted(list(set(i))) != list(range(1, n**2+1)):
            f = False
            break

    for k in range(n):
        for i in range(n, n**2 + n, n):
            s = set()
            for j in range(n):
                s.update(a[n*k+j][i-n:i])
            if sorted(list(s)) != list(range(1, n**2+1)):
                f = False
                break

    if f:
        print(f"Case #{t+1}: Yes")
    else:
        print(f"Case #{t+1}: No")
