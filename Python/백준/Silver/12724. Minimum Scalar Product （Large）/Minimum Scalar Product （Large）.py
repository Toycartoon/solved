for t in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.sort()
    y.sort(reverse=True)

    v = 0
    for i in range(n):
        v += x[i] * y[i]
    print(f"Case #{t+1}: {v}")
