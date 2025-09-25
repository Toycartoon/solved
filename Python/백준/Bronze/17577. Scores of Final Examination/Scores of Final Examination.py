while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    v = []
    for i in range(m):
        v.append(list(map(int, input().split())))
    
    ans = []
    for i in zip(*v):
        ans.append(sum(i))
    print(max(ans))
