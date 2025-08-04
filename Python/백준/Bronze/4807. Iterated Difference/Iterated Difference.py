import sys

input = sys.stdin.readline

t = 1
while True:
    n = int(input())
    if n == 0:
        break

    a = list(map(int, input().split()))
    ans = 0
    while a.count(a[0]) != n and ans <= 1000:
        na = []
        for i in range(n):
            na.append(abs(a[i % n] - a[(i+1) % n]))
        a = na
        ans += 1

    if ans > 1000:
        print(f"Case {t}: not attained")
    else:
        print(f"Case {t}: {ans} iterations")
    t += 1
