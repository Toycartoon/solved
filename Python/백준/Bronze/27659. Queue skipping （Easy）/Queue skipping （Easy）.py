for t in range(int(input())):
    _ = input()
    n, e = map(int, input().split())
    a = [i for i in range(n)]

    idx = 0
    for x in range(e):
        m = int(input())
        a[m-1] = idx
        idx -= 1
    print(a.index(max(a))+1)
