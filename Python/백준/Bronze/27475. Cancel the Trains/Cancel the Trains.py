import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in a:
        if i in b:
            ans += 1

    print(ans)
