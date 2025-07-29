import sys

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    ans = [True for _ in range(n)]
    ans[m-1] = False
    for i in range(n-2):
        ans[int(input())-1] = False

    print(ans.index(True) + 1)
