import sys

input = sys.stdin.readline

for i in range(int(input())):
    s, n, f, m = map(int, input().split())
    if n <= s-m <= n * f:
        print("YES")
    else:
        print("NO")
