w, n = input().split()
g = [list(map(int, input().split())) for _ in range(int(n))]

def check(n):
    if n == 1:
        return 1
    elif n == 2:
        return 5
    elif n == 5:
        return 2
    elif n == 8:
        return 8
    else:
        return "?"

if w == "L" or w == "R":
    for i in g:
        for v in i[::-1]:
            print(check(v), end=" ")
        print()
elif w == "U" or w == "D":
    for i in g[::-1]:
        for v in i:
            print(check(v), end=" ")
        print()
