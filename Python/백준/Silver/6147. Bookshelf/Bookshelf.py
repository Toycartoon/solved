import sys

input = sys.stdin.readline

n, b = map(int, input().split())
h = []
for i in range(n):
    h.append(int(input()))
h.sort(reverse=True)

ans = 0
for i in h:
    if b > 0:
        b -= i
        ans += 1
    else:
        break
print(ans)
