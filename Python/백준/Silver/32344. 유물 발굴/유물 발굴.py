import sys

input = sys.stdin.readline

r, c = map(int, input().split())
w = {}
for n in range(int(input())):
    a, v, h = map(int, input().split())
    if a in w:
        mnv, mnh, mxv, mxh = w[a]
        w[a] = (min(mnv, v), min(mnh, h), max(mxv, v+1), max(mxh, h+1))
    else:
        w[a] = (v, h, v+1, h+1)

ans = (0, -float('inf'))
for k in w.keys():
    mnv, mnh, mxv, mxh = w[k]
    ans = max(((mxv-mnv)*(mxh-mnh), -k), ans)

print(-ans[1], ans[0])
