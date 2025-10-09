import sys

input = sys.stdin.readline

a = []
for i in range(int(input())):
    a.append(int(input()))

a.sort()
ans = float('inf')
for i in range(len(a) // 2 + 1):
    ans = min(ans, a[i] + a[-i-1])
print(ans)
