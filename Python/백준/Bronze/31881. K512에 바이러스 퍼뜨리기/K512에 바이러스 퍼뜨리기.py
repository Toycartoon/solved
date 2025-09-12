import sys

input = sys.stdin.readline

n, q = map(int, input().split())
s = set()
for i in range(q):
    c, *x = map(int, input().split())
    if c == 1:
        s.add(x[0])
    elif c == 2:
        if x[0] in s:
            s.remove(x[0])
    elif c == 3:
        print(n-len(s))
