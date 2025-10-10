for t in range(int(input())):
    s = input().split()
    for i in s:
        print(chr(i.count("M") * 16 + i.count("O")), end="")
    print()
