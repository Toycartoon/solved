import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, k = map(int, input().split())

    if k == 1 and (n == 2 or n == 3):
        print(-1)
        continue

    if k != 1:
        print(*range(1, n+1))
    else:
        print(*range(2, n+1, 2), *range(1, n+1, 2))
