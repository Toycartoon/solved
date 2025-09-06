r, c = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(r)]
t = int(input())

k = 0
for y in range(r-2):
    for x in range(c-2):
        v = []
        for i in range(3):
            for j in range(3):
                v.append(g[y+i][x+j])
        v.sort()
        if v[4] >= t:
            k += 1

print(k)
