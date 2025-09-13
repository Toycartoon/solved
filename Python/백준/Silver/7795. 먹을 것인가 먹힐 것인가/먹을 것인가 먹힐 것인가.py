import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()
    ans = 0
    for i in a:
        l, r = -1, m
        while l + 1 < r:
            mid = (l + r) // 2
            if i > b[mid]:
                l = mid
            else:
                r = mid
        ans += r
    print(ans)
