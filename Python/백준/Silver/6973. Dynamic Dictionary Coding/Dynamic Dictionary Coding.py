import sys

input = sys.stdin.readline

n = int(input())
t = 0
w = {}
idx = 1
while t < n:
    s = input().strip()
    if len(s) == 0:
        t += 1
        w.clear()
        idx = 1
        print()
        continue

    for i in s.split():
        if i in w:
            print(w[i], end=" ")
        else:
            print(i, end=" ")
            w[i] = idx
            idx += 1
    print()
