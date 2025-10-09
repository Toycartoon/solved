while True:
    n = int(input())
    if n == 0:
        break

    a = list(map(int, input().split()))
    a.sort()

    v = a[0]
    length = 1
    ans = []
    for i in range(1, len(a)):
        if a[i] == v+1:
            v += 1
            length += 1
        else:
            v = a[i]
            ans.append(length)
            length = 1
    ans.append(length)
    print(max(ans))
