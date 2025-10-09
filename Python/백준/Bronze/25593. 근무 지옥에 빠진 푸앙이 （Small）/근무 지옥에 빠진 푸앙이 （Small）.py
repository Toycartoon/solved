import sys

input = sys.stdin.readline

n = int(input())
w = {}
for i in range(n):
    for x in range(4):
        a = input().strip().split()
        for v in a:
            if v == "-":
                continue
            if v in w:
                w[v] += (4, 6, 4, 10)[x]
            else:
                w[v] = (4, 6, 4, 10)[x]

if len(w) == 0:
    print("Yes")
    exit()

if max(w.values()) - min(w.values()) <= 12:
    print("Yes")
else:
    print("No")
