for t in range(int(input())):
    n, *a = map(int, input().split())
    for i in range(1, n):
        if a[i-1] + 1 != a[i]:
            print(i+1)
            break
