v = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
for i in range(int(input())):
    a = int(input())
    f = False
    for x in v:
        if a-x in v:
            f = True
            break

    if f:
        print("Yes")
    else:
        print("No")
