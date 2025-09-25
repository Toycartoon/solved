for t in range(int(input())):
    a = [chr(i) for i in range(97, 123)]
    n = int(input())
    x = list(map(int, input().split()))

    for i in x:
        v = a.pop(i)
        print(v, end='')
        a.insert(0, v)
    print()
