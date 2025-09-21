import sys

input = sys.stdin.readline

n = int(input())
s = input().strip()
x, y = 0, 0
l = [(x, y)]
for i in s:
    if i == "E":
        x += 1
    elif i == "W":
        x -= 1
    elif i == "S":
        y -= 1
    elif i == "N":
        y += 1
    l.append((x, y))

s = 0
for i in range(n):
    s += l[i][0] * l[i+1][1]

for i in range(n):
    s -= l[i][1] * l[i+1][0]

print(abs(s // 2))
