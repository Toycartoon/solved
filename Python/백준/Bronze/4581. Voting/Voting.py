while True:
    s = input()
    if s == "#":
        break

    if s.count("A") >= len(s) / 2:
        print("need quorum")
    elif s.count("Y") > s.count("N"):
        print("yes")
    elif s.count("Y") < s.count("N"):
        print("no")
    elif s.count("Y") == s.count("N"):
        print("tie")
