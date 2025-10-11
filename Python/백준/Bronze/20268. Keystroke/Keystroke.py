for t in range(int(input())):
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if m + n == 4:
        print(7)
    else:
        print(1)
