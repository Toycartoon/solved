import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ps = [0]
    v = 0
    for i in a:
        v += i
        ps.append(v)

    ans = -float('inf')
    for i in range(1, len(ps)):
        for j in range(i, len(ps)):
            ans = max(ps[j] - ps[j-i], ans)
    print(ans)
