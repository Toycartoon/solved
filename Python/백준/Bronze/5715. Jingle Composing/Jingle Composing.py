w = {"W": 64, "H": 32, "Q": 16, "E": 8, "S": 4, "T": 2, "X": 1}
while True:
    s = input().split("/")
    if s == ["*"]:
        break

    ans = 0
    for i in s:
        a = 0
        for v in i:
            a += w[v]

        if a == 64:
            ans += 1
    print(ans)
