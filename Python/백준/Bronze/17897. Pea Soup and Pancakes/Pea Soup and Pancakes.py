for n in range(int(input())):
    k = int(input())
    name = input()
    ps, pa = False, False
    for i in range(k):
        s = input()
        if s == "pea soup":
            ps = True
        elif s == "pancakes":
            pa = True

    if ps and pa:
        print(name)
        exit()
print("Anywhere is fine I guess")
