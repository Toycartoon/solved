for i in range(int(input())):
    a, b = input().split()
    if {*a} != {*b}:
        print("NO")
    else:
        print("YES")
