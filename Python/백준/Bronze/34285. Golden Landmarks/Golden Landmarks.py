import sys

input = sys.stdin.readline

w = {}
for i in range(int(input())):
    l, x, y = input().split()
    w[l] = (int(x), int(y))

s = input().strip().split()
ans = 0
for i in range(1, len(s)):
    ans += abs(w[s[i-1]][0] - w[s[i]][0]) + abs(w[s[i-1]][1] - w[s[i]][1])

print(ans)
