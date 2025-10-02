n = input()
a = []
for i in n:
    s = bin(int(i))[2:].zfill(4).replace("1", "*").replace("0", ".")
    a.append([*s])

a = list(zip(*a))
for i in range(4):
    print("{} {}   {} {}".format(*a[i]))
