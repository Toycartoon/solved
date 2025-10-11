import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(n):
        x, y = map(int, input().split())
        d = (x ** 2 + y ** 2) ** 0.5
        for x in range(1, 11):
            if 20 * x >= d:
                ans += 11 - x
                break
    print(ans)
