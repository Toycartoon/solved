import sys

input = sys.stdin.readline

n, q = map(int, input().split())
ans = 0

s = []
for i in range(n):
    s.append("SciComLove"[i % 10])
    if i % 10 == 0 or i % 10 == 3 or i % 10 == 6:
        ans += 1

for i in range(q):
    x = int(input())
    if s[x-1].isupper():
        s[x-1] = s[x-1].lower()
        ans -= 1
    else:
        s[x-1] = s[x-1].upper()
        ans += 1
    print(ans)
