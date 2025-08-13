while True:
    n = int(input())
    if n == 0:
        break

    s = "".join(input().split()).upper()
    ans = ["" for _ in range(len(s))]

    v = 0
    for idx in range(len(s)):
        if v >= len(ans):
            v = ans.index("")

        ans[v] = s[idx]
        v += n

    print(*ans, sep="")
