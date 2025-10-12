import sys

input = sys.stdin.readline

for t in range(int(input())):
    w = {}
    for i in range(int(input())):
        s, n = input().split()
        if s in w:
            w[s] = min(w[s], int(n))
        else:
            w[s] = int(n)
    print(*sorted(w.values()))
