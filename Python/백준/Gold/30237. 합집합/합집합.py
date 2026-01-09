import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())

    s = []
    union = set()

    ans = 0
    for i in range(n):
        m, *k = map(int, input().split())
        s.append(set(k))
        union.update(set(k))

    for i in range(1, 51):
        x = set()
        for v in s:
            if i in v:
                continue
            x.update(v)
        if len(x) != len(union):
            ans = max(ans, len(x))
    print(ans)
