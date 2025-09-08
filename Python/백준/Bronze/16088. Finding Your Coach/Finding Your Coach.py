for i in range(int(input())):
    l, r, n, m = map(int, input().split())
    if n == m:
        print("G")
    elif abs(n-m) <= l and abs(n-m) <= r:
        print("E")
    elif abs(n-m) <= l:
        print("L")
    elif abs(n-m) <= r:
        print("R")
