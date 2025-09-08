import sys

input = sys.stdin.readline

for t in range(int(input())):
    a = []
    for n in range(int(input())):
        a.append(input())
    s = input().strip().upper()

    print(f"Data Set {t+1}:")
    for i in a:
        f = True
        x = i.upper()
        for v in s:
            if v in x:
                x = x[x.index(v)+1:]
            else:
                f = False
                break

        if f:
            print(i, end="")
