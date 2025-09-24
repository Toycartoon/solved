while True:
    n = int(input())
    if n == 0:
        break

    s = []
    idx = 0
    for i in range(n):
        c, x = input().split()
        if c == "INSERT":
            s.insert(idx, x)
            idx += 1
        elif c == "LEFT":
            idx = max(0, idx-1)
        elif c == "RIGHT":
            idx = min(len(s), idx+1)
    print("".join(s))
