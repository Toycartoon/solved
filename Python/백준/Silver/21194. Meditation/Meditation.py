import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

a.sort(reverse=True)
ans = 0
for i in range(k):
    ans += a[i]

print(ans)
