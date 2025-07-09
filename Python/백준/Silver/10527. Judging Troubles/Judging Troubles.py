import sys

input = sys.stdin.readline

n = int(input())
a = {}
for i in range(n):
    s = input().strip()

    if s in a:
        a[s] += 1
    else:
        a[s] = 1

ans = 0
for i in range(n):
    s = input().strip()

    if s in a:
        if a[s] >= 1:
            ans += 1
            a[s] -= 1

print(ans)
