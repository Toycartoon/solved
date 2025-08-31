k = [[*input()] for _ in range(4)]
s = input()

for y in range(1, 3):
    for x in range(1, 9):
        if len({k[y-1][x-1], k[y-1][x], k[y+1][x+1], k[y][x-1], k[y][x], k[y][x+1], k[y+1][x-1], k[y+1][x], k[y+1][x+1]} - {*s}) == 0:
            print(k[y][x])
            exit()
