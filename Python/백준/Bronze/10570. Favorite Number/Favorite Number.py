import sys

input = sys.stdin.readline

for n in range(int(input())):
    v = int(input())
    w = {}

    for i in range(v):
        s = int(input())
        if s in w:
            w[s] += 1
        else:
            w[s] = 1

    print(sorted(w.items(), key=lambda x: (-x[1], x[0]))[0][0])
