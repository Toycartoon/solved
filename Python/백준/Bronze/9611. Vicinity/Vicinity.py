import sys

input = sys.stdin.readline

a = []
for i in range(int(input())):
    x, y = map(int, input().split())
    a.append((x, y))

for _ in range(int(input())):
    i, d = map(int, input().split())
    ans = 0
    for j in range(len(a)):
        if i-1 == j:
            continue
        v = ((a[i-1][0]-a[j][0]) ** 2 + (a[i-1][1]-a[j][1]) ** 2) ** 0.5
        if v <= d:
            ans += 1
    print(ans)
