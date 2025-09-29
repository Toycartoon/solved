w, h = map(int, input().split())
a = [[*input()] for _ in range(h)]
b = [[*input()] for _ in range(h)]
d = input()
for y in range(h):
    for x in range(w):
        if a[y][x] == "0" and b[y][x] == "0":
            print(d[0], end="")
        elif a[y][x] == "0" and b[y][x] == "1":
            print(d[1], end="")
        elif a[y][x] == "1" and b[y][x] == "0":
            print(d[2], end="")
        elif a[y][x] == "1" and b[y][x] == "1":
            print(d[3], end="")
    print()
