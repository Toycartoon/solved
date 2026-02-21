import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())
w = {}
for i in range(m):
    a, b, c = map(int, input().split())
    if (a, b) not in w:
        w[(a, b)] = c
        w[(b, a)] = c
    else:
        if w[(a, b)] > c:
            w[(a, b)] = c
            w[(b, a)] = c

for i in range(q):
    s, e = map(int, input().split())
    if (s, e) in w:
        print(w[(s, e)])
    else:
        print(-1)
