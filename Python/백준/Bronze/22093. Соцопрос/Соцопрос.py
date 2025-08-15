for t in range(int(input())):
    n, a, b = map(int, input().split())
    print(max(0, a-b), min(n-b, a))
