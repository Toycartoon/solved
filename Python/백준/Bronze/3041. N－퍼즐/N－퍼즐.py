g = [[*input()] for _ in range(4)]
ans = 0
for r in range(4):
    for c in range(4):
        f = True
        for y in range(4):
            for x in range(4):
                if not f:
                    break
                
                if g[y][x] == chr(65 + r * 4 + c):
                    ans += abs(r-y) + abs(c-x)
                    f = False
                    break
print(ans)
