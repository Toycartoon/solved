for t in range(int(input())):
    l, r, s = map(int, input().split())
    print(min((r-s) * 2 - 1, (s-l) * 2)+1)
