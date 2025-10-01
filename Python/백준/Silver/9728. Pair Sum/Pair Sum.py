import sys

input = sys.stdin.readline

for t in range(int(input())):
    w = {}

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for i in a:
        if i in w:
            w[i] += 1
        else:
            w[i] = 1

    ans = 0
    for i in w.keys():
        if i * 2 <= m:
            if m-i in w:
                ans += w[i] * w[m-i]
    print(f"Case #{t+1}: {ans}")
