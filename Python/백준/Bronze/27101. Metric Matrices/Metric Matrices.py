n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for x in range(n):
    if a[x][x] != 0:
        print(1)
        exit()

for y in range(n):
    for x in range(n):
        if x != y and a[x][y] <= 0:
            print(2)
            exit()

for y in range(n):
    for x in range(n):
        if a[x][y] != a[y][x]:
            print(3)
            exit()

for z in range(n):
    for y in range(n):
        for x in range(n):
            if a[x][y] + a[y][z] < a[x][z]:
                print(4)
                exit()
print(0)
