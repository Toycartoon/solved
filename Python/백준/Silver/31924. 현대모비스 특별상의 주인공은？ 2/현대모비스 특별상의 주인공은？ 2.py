n = int(input())
g = [[*input()] for _ in range(n)]

pos = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
ans = 0
s = "MOBIS"
for y in range(n):
    for x in range(n):
        if g[y][x] == "M":
            for dx, dy in pos:
                f = True
                for w in range(1, 5):
                    if 0 <= y+dy*w < n and 0 <= x+dx*w < n:
                        if g[y+dy*w][x+dx*w] != s[w]:
                            f = False
                            break
                    else:
                        f = False
                        break
                if f:
                    ans += 1
print(ans)
