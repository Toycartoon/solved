for t in range(int(input())):
    s = input()

    a = {*s}
    if len(a) != 2 or len(s) != 7:
        print(0)
        continue

    s = s.replace(a.pop(), "0").replace(a.pop(), "1")
    print(int(s == "0011011" or s == "1100100"))
