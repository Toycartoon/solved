import sys

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    g = [list(map(int, input().split())) for _ in range(n)]
    w = {}
    for _ in g:
        for i in _:
            if i in w:
                w[i] += 1
            else:
                w[i] = 1

    s = {*w.values()}
    mx = max(s-{max(s)})

    ans = []
    for i in w.keys():
        if w[i] == mx:
            ans.append(i)
    print(*sorted(ans))
