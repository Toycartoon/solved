for t in range(int(input())):
    shirt = []
    pants = []
    socks = []
    for i in range(int(input())):
        s = input().split()
        if s[-1] == "(shirt)":
            shirt.append(" ".join(s[:-1]))
        elif s[-1] == "(pants)":
            pants.append(" ".join(s[:-1]))
        elif s[-1] == "(socks)":
            socks.append(" ".join(s[:-1]))

    v = min(len(shirt), len(pants), len(socks))
    for i in range(v):
        print(f"{shirt.pop()}, {pants.pop()}, {socks.pop()}")
    print()
