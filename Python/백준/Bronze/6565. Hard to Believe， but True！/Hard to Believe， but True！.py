while True:
    s = input()
    if s == "0+0=0":
        print(True)
        break
    ans, x = s[::-1].split("=")
    a, b = map(int, x.split("+"))
    print(a + b == int(ans))
