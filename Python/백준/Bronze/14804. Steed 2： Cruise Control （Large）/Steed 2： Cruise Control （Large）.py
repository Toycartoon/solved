import sys

input = sys.stdin.readline

for t in range(int(input())):
    d, n = map(int, input().split())

    ans = float('inf')
    for i in range(n):
        k, s = map(int, input().split())
        ans = min(ans, d / ((d-k) / s))
    print(f"Case #{t+1}: {ans}")
