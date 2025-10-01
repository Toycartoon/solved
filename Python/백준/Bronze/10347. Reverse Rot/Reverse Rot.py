while True:
    n, *s = input().split()
    if n == "0":
        break

    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    for i in s[0][::-1]:
        print(a[(a.index(i)+int(n)) % len(a)], end="")
    print()
