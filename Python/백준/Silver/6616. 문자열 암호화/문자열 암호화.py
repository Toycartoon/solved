while True:
    n = int(input())
    if n == 0:
        break

    s = "".join(input().split()).upper()
    ans = ["" for _ in range(len(s))]

    idx = 0
    v = 0
    while idx < len(s):
        if v >= len(ans):
            v = ans.index("")

        ans[v] = s[idx]
        idx += 1
        v += n

    print(*ans, sep="")
