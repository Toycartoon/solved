import sys

input = sys.stdin.readline

w = {}
for i in range(int(input())):
    s, k = input().strip().split()

    if s in w:
        w[s] += int(k)
    else:
        w[s] = int(k)

for i in sorted(w.keys()):
    print(i, w[i])
