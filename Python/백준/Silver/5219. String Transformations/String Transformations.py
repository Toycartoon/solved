for t in range(int(input())):
    s = input().split()
    a = []
    for i in range(0, len(s), 2):
        a.append((s[i], s[i+1]))

    s = input().split()
    print("Transformed strings: ", end="")
    for i in s:
        ns = i
        for v in range(len(a)):
            x = ns.replace(a[v][0], a[v][1], 1)
            if x == ns:
                break
            ns = x
        print(ns, end=" ")
    print()
