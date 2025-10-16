while True:
    n = int(input())
    if n == 0:
        break

    s = input().split(",")
    ans = [False for _ in range(n+1)]
    for i in s:
        if "-" in i:
            l, r = map(int, i.split("-"))
        else:
            l, r = int(i), int(i)

        if l > r:
            continue

        for x in range(min(len(ans), l), min(len(ans), r+1)):
            ans[x] = True
    print(ans.count(True))
