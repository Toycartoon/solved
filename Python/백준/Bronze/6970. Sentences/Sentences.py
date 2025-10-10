for _ in range(int(input())):
    a = int(input())
    b = int(input())
    c = int(input())

    sub = []
    for i in range(a):
        sub.append(input())

    verb = []
    for i in range(b):
        verb.append(input())

    obj = []
    for i in range(c):
        obj.append(input())

    for i in sub:
        for j in verb:
            for k in obj:
                print(f"{i} {j} {k}.")
    print()
