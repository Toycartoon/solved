import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    v = []
    for i in range(n):
        _, *x, money = map(int, input().split())
        v.append((x, money))
    a = list(map(int, input().split()))

    ans = 0
    for idx, money in v:
        mn = float('inf')
        for i in idx:
            mn = min(mn, a[i-1])
        ans += money * mn
    print(ans)
