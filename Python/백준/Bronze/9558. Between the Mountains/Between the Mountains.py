import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, *a = map(int, input().split())
    m, *b = map(int, input().split())

    ans = float('inf')
    for i in a:
        for j in b:
            ans = min(ans, abs(i-j))
    print(ans)
