for k in range(int(input())):
    n = int(input())
    a = [0]
    for i in range(n-1):
        a.append(int(input()))

    v = []
    for i in range(n):
        v.append(input())

    s = input()
    e = input()
    print(f"Data Set {k+1}:")
    print(a[abs(v.index(s)-v.index(e))])
    print()
