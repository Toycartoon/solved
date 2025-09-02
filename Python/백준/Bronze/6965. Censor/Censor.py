for t in range(int(input())):
    s = input().split()
    for i in s:
        if len(i) != 4:
            print(i, end=" ")
        else:
            print("****", end=" ")
    print("\n")
