n = int(input())
a = input()
b = input()

for i in range(n):
    if a[i] == b[i]:
        if a[i] == "R":
            print("P", end="")
        elif a[i] == "S":
            print("R", end="")
        elif a[i] == "P":
            print("S", end="")
    else:
        if a[i] == "R":
            if b[i] == "S":
                print("R", end="")
            elif b[i] == "P":
                print("P", end="")
        elif a[i] == "S":
            if b[i] == "R":
                print("R", end="")
            elif b[i] == "P":
                print("S", end="")
        elif a[i] == "P":
            if b[i] == "S":
                print("S", end="")
            elif b[i] == "R":
                print("P", end="")
