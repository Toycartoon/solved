while True:
    n, k = map(int, input().split())
    if n == k == 0:
        break
    b, s = 1, k
    for i in range(n):
        h, status = input().split()
        if status == "SAFE":
            b = max(b, int(h))
        elif status == "BROKEN":
            s = min(s, int(h))
    print(b+1, s-1)
