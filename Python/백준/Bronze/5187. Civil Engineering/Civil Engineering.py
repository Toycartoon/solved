import sys

input = sys.stdin.readline

for k in range(int(input())):
    m, n = map(int, input().split())
    a = []
    for i in range(m):
        a.append(int(input()))

    ans = 0
    for _ in range(n):
        h, w, d, i = map(int, input().split())
        ans += h * w * d * a[i-1]

    print(f"Data Set {k+1}:")
    print(ans)
