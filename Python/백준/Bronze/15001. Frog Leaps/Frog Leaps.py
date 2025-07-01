import sys

input = sys.stdin.readline

n = int(input())
x = []
for i in range(n):
    x.append(int(input()))

ans = 0
for i in range(1, n):
    ans += (x[i] - x[i-1]) ** 2

print(ans)
