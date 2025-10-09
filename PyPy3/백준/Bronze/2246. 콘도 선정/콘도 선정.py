import sys

input = sys.stdin.readline

a = []
for i in range(int(input())):
    d, c = map(int, input().split())
    a.append((d, c))

ans = 0
a.sort()
for i in range(len(a)):
    f = True
    for j in range(len(a)):
        if i == j:
            continue
        if (a[i][0] > a[j][0] and a[j][1] <= a[i][1]) or (a[i][1] > a[j][1] and a[i][0] >= a[j][0]):
            f = False
            break
    if f:
        ans += 1
print(ans)
