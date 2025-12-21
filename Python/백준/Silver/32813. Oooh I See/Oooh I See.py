r, c = map(int, input().split())
g = [[*input()] for _ in range(r)]

ans = []
for y in range(1, r-1):
    for x in range(1, c-1):
        if g[y][x] == "0" and g[y-1][x] == g[y][x-1] == g[y-1][x-1] == g[y+1][x-1] == g[y+1][x] == g[y+1][x+1] == g[y][x+1] == g[y-1][x+1] == "O":
            ans.append((y+1, x+1))

if len(ans) == 1:
    print(*ans[0])
elif len(ans) == 0:
    print("Oh no!")
else:
    print(f"Oh no! {len(ans)} locations")
