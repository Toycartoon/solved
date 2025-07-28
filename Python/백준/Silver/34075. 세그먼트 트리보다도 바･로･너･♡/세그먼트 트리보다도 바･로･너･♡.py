import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    s, d = input().split()
    a.append((s, int(d)))

m = {}
for i in range(int(input())):
    n, t = input().split()
    m[n] = int(t)

a = sorted(sorted(a, key=lambda x: x[0], reverse=True), key=lambda x: x[1])

s = 0
for _ in range(int(input())):
    x, y, z = input().strip().split()

    if z == "chan!":
        print("hai!")
        s = m[x]
    elif z == "suki?":
        p = (abs(a[0][1]-s), a[0][0])
        idx = 0
        for i in range(len(a)):
            if abs(a[i][1]-s) < p[0] or (abs(a[i][1]-s) == p[0] and min(a[i][0], p[1]) != p[1]):
                p = (abs(a[i][1]-s), a[i][0])
                idx = i

        q = (abs(a[0][1]-s), a[0][0]) if idx != 0 else (abs(a[1][1]-s), a[1][0])
        for i in range(len(a)):
            if i == idx:
                continue
            if abs(a[i][1]-s) < q[0] or (abs(a[i][1]-s) == q[0] and min(a[i][0], q[1]) != q[1]):
                q = (abs(a[i][1]-s), a[i][0])

        print(f"{q[1]} yori mo {p[1]}")
