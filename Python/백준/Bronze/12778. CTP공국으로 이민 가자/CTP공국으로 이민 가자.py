for t in range(int(input())):
    m, s = input().split()
    a = input().split()

    if s == "C":
        for i in a:
            print(ord(i)-64, end=" ")
    elif s == "N":
        for i in a:
            print(chr(int(i)+64), end=" ")
    print()
