import sys

input = sys.stdin.readline

n, k = map(int, input().split())
for i in range(k):
    s, t, r = map(int, input().split())
    a = n
    ans = 0
    while a > 0:
        for i in range(t):
            a -= s
            ans += 1
            if a <= 0:
                break
        if a <= 0:
            break
        ans += r

    print(ans)
