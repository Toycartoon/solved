w = {}
n = int(input())
for i in range(n):
    me, mn = map(int, input().split())
    w[me] = mn

for r in range(int(input())):
    l, *s = map(int, input().split())
    output = []
    f = True
    for i in s:
        if i in w:
            output.append(w[i])
        else:
            f = False
            break

    if f:
        print(*output)
    else:
        print("YOU DIED")
