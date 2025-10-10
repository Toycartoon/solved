for t in range(int(input())):
    k = int(input())
    a = input()
    b = input()
    d = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            d += 1
    print(len(a) - abs(k-d))
