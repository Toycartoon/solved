t = 1
while True:
    u, v = input().split()
    if u == v == "#":
        break

    print(f"Case {t}")
    for i in range(int(input())):
        s = input().replace(u, "_").replace(v, "_").replace(u.upper(), "_").replace(v.upper(), "_")
        print(s)
    print()
    t += 1
