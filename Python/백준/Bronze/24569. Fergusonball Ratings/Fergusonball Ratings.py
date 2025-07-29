import sys

input = sys.stdin.readline

ans = 0
t = int(input())
for _ in range(t):
    n = int(input())
    m = int(input())
    if n * 5 - m * 3 > 40:
        ans += 1

print(ans, "+" if ans == t else "", sep="")
