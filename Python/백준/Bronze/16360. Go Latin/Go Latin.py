for t in range(int(input())):
    s = input()
    if s.endswith("a") or s.endswith("o") or s.endswith("u"):
        print(s + "s")
    elif s.endswith("i") or s.endswith("y"):
        print(s[:-1] + "ios")
    elif s.endswith("l") or s.endswith("r") or s.endswith("v"):
        print(s + "es")
    elif s.endswith("n"):
        print(s[:-1] + "anes")
    elif s.endswith("ne"):
        print(s[:-2] + "anes")
    elif s.endswith("t") or s.endswith("w"):
        print(s + "as")
    else:
        print(s + "us")
