for t in range(int(input())):
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    j = len(a & b) / len(a | b)
    print(int(j + 0.5))
