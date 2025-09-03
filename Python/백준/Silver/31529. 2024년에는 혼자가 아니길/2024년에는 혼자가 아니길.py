x, y = map(int, input().split())
w = 2 * x - y
if w < 0 or y < x:
    print(-1)
else:
    print(506 * w)
