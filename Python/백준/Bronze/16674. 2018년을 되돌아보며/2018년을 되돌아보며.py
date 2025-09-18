n = input()
if len({*n} - {"2", "0", "1", "8"}) != 0:
    print(0)
elif len({*n} & {"2", "0", "1", "8"}) != 4:
    print(1)
elif n.count("2") == n.count("0") == n.count("1") == n.count("8"):
    print(8)
else:
    print(2)
