for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    while len(a) > 2:
        na = []
        for i in range(len(a) // 2 + 1):
            na.append(a[i]+a[-i-1])
        a = na

    if a[0] > a[1]:
        print(f"Case #{t+1}: Alice")
    else:
        print(f"Case #{t+1}: Bob")
