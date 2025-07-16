for t in range(int(input())):
    s = input()
    c = input()

    for i in s:
        if i.isalpha():
            print(c[ord(i)-65], end="")
        else:
            print(i, end="")
    print()
