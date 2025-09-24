while True:
    joe, james, jean, jane, none = 0, 0, 0, 0, 0
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        s = input()
        if s.isnumeric():
            if int(s) >= 12:
                jean += 1
            else:
                jane += 1
        elif s in ("M", "L"):
            joe += 1
        elif s == "S":
            james += 1
        else:
            none += 1
    print(joe, jean, jane, james, none)