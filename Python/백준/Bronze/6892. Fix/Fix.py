for _ in range(int(input())):
    a = []
    for __ in range(3):
        a.append(input())

    f = True
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if a[i].startswith(a[j]) or a[i].endswith(a[j]):
                f = False
                break

    if f:
        print("Yes")
    else:
        print("No")
