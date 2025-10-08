for t in range(int(input())):
    _ = input()
    n, m = map(int, input().split())
    s = set(input().split())
    s.update(input().split())
    print(len(s))
