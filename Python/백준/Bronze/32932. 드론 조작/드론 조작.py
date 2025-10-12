s = set()
n, k = map(int, input().split())
for i in range(n):
    xi, yi = map(int, input().split())
    s.add((xi, yi))

x, y = 0, 0
for i in input():
    if i == "U":
        if (x, y+1) not in s:
            y += 1
    elif i == "D":
        if (x, y-1) not in s:
            y -= 1
    elif i == "R":
        if (x+1, y) not in s:
            x += 1
    elif i == "L":
        if (x-1, y) not in s:
            x -= 1
print(x, y)
