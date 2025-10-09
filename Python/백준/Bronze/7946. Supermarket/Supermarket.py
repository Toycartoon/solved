for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(a[k-1])
