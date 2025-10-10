import sys

input = sys.stdin.readline

ans = (0, 1)
q = 0
for i in range(int(input())):
    com, *n = map(int, input().split())
    if com == 1:
        ans = max((q+1, -n[0]), ans)
        q += 1
    elif com == 2:
        q -= 1
print(ans[0], -ans[1])
