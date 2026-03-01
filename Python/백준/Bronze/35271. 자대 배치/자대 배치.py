n, m = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(n):
    x = list(map(int, input().split()))
    f = True
    for i in x:
        if a[i-1] > 0:
            a[i-1] -= 1
            f = False
            print(i, end=" ")
            break

    if f:
        print(-1, end=" ")
