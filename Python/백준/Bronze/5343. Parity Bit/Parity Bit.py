for i in range(int(input())):
    s = input()

    ans = 0
    for v in range(7, len(s), 8):
        if s[v-7:v].count("1") % 2 != int(s[v]):
            ans += 1

    print(ans)
