import sys

input = sys.stdin.readline

n, q = map(int, input().split())
s = [*input().strip()]
for i in range(q):
    com, x, *y = map(int, input().split())

    if com == 1:
        if s[x-1] == "0":
            s[x-1] = "1"
        else:
            s[x-1] = "0"
    elif com == 2:
        f = y[0]-x+1 >= 4
        if not f:
            for p in range(x, y[0]):
                if s[p] == s[p-1]:
                    f = True
                    break

        if f:
            print("YES")
        else:
            print("NO")
