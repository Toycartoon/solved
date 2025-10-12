while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    a = []
    for i in range(n):
        a.append(int(input()))

    b = []
    for i in range(m):
        b.append(int(input()))

    sa = sum(a)
    sb = sum(b)
    ans = (float('inf'), float('inf'))
    for i in a:
        for j in b:
            if sa-i+j == sb-j+i:
                if i+j < sum(ans):
                    ans = (i, j)

    if ans[0] == float('inf'):
        print(-1)
    else:
        print(*ans)
