import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for i in range(n):
    s, v = input().split()
    a.append((int(v), s))

for i in range(m):
    x = int(input())
    l, r = -1, n
    while l + 1 < r:
        mid = (l + r) // 2
        if a[mid][0] < x:
            l = mid
        else:
            r = mid
    print(a[r][1])
