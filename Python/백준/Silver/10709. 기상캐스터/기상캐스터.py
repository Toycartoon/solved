h, w = map(int, input().split())
a = [[*input()] for _ in range(h)]
ans = [[-1 for _ in range(w)] for __ in range(h)]

for y in range(h):
    for x in range(w):
        if a[y][x] == "c":
            ans[y][x] = 0
        else:
            if ans[y][x-1] != -1:
                ans[y][x] = ans[y][x-1] + 1

for i in ans:
    print(*i)
