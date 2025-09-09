import sys

input = sys.stdin.readline

ans = 0
for i in range(int(input())):
    _, c, n = input().split()
    if c == "IN":
        ans += int(n)
    elif c == "OUT":
        ans -= int(n)

print(ans if ans != 0 else "NO STRAGGLERS")
