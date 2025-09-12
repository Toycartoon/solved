import sys

input = sys.stdin.readline

n = int(input())
b = input().strip()
ans = 0
for i in range(n-1):
    s = input().strip()
    ans += abs(ord(b[0]) - ord(s[0])) + abs(ord(b[1]) - ord(s[1]))
    b = s

print(ans)
