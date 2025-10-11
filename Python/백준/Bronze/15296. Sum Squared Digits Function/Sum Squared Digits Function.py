import sys

input = sys.stdin.readline

for p in range(int(input())):
    k, b, n = map(int, input().split())
    ans = 0
    while n > 0:
        ans += (n % b) ** 2
        n //= b
    print(k, ans)
