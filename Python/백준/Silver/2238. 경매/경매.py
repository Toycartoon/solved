import sys

input = sys.stdin.readline

u, n = map(int, input().split())
a = [(0, i, "") for i in range(u+1)]
for i in range(n):
    s, p = input().strip().split()
    if a[int(p)][0] == 0:
        a[int(p)] = (1, int(p), s)
    else:
        a[int(p)] = (a[int(p)][0]+1, int(p), a[int(p)][2])

a.sort(key=lambda x: (x[0], x[1]))
for i in range(len(a)):
    if a[i][0] != 0:
        print(a[i][2], a[i][1])
        break
