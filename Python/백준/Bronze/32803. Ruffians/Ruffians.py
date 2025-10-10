for t in range(int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    f = False
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                continue
            if a[i] == b[j]:
                f = True
                break
    if f:
        print("YES")
    else:
        print("NO")
