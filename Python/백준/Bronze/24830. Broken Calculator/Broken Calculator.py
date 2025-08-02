c = 1
for t in range(int(input())):
    a, op, b = input().split()

    if op == "+":
        c = int(a) + int(b) - c
    elif op == "-":
        c = (int(a) - int(b)) * c
    elif op == "*":
        c = (int(a) * int(b)) ** 2
    elif op == "/":
        if int(a) % 2 == 0:
            c = int(a) // 2
        else:
            c = (int(a) + 1) // 2
    print(c)
