u = set()
for i in range(int(input())):
    u.add(input())

f = False
for i in range(int(input())):
    s = input()
    if s in u:
        if f:
            print(f"Closed by {s}")
        else:
            print(f"Opened by {s}")
        f = not f
    else:
        print(f"Unknown {s}")
