import sys

input = sys.stdin.readline

n = int(input())
v = []
for i in range(n):
    a, l = map(int, input().split())
    v.append((a, l))

v.sort()
ans = 1
for i in range(1, n):
    if v[i-1][0] + v[i-1][1] < v[i][0]:
        ans += 1

print(ans)
