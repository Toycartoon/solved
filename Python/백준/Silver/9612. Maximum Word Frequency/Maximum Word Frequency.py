import sys

input = sys.stdin.readline

w = {}
for i in range(int(input())):
    s = input().strip()
    if s in w:
        w[s] += 1
    else:
        w[s] = 1

print(*sorted(w.items(), key=lambda x: (x[1], x[0]))[-1])
