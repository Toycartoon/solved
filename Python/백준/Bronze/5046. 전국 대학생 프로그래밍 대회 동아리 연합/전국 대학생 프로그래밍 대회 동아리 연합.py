import sys

input = sys.stdin.readline

n, b, h, w = map(int, input().split())
ans = []
for i in range(h):
    p = int(input())
    if max(list(map(int, input().split()))) >= n:
        ans.append(n * p)

if len(ans) == 0 or min(ans) > b:
    print("stay home")
else:
    print(min(ans))
