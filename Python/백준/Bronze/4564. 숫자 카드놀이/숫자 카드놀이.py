while True:
    n = int(input())
    if n == 0:
        break

    ans = [n]
    while len(str(n)) > 1:
        v = 1
        for i in str(n):
            v *= int(i)
        ans.append(v)
        n = v

    print(*ans)
