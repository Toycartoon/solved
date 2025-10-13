import sys

input = sys.stdin.readline

x = 0
ans = 0
for a in range(int(input())):
    i, p, m = map(int, input().split())
    if p != x:
        print("INVALID")
        exit()
    x = i
    ans += m
    if ans < 0:
        print("NO_MONEY")
        exit()
print(ans)