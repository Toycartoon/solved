for i in range(int(input())):
    s = input()
    ans = ""
    for v in s:
        x = ord(v) + 13
        if x > 122:
            x -= 26
        ans += chr(x)
    print(ans)
