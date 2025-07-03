import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
w = {}
for i in range(n):
    s, p = input().strip().split()
    w[s] = int(p)

mn, mx = 0, 0
for i in range(k):
    s = input().strip()
    mn += w[s]
    mx += w[s]

    del w[s]

v = sorted(list(w.values()))
mn += sum(v[:m-k]) if m - k != 0 else 0
mx += sum(v[-m+k:]) if m - k != 0 else 0

print(mn, mx)
