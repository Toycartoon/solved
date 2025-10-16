p = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    p.append([x, y])

p.sort()
for i in range(n):
    print(p[i][0], p[i][1])