import sys

input = sys.stdin.readline

n, q = map(int, input().split())
s = [*input().strip()]
for i in range(n):
    s[i] = ord(s[i]) - 65

for _ in range(q):
    com, l, r = map(int, input().split())

    if com == 1:
        ans = 1
        for i in range(l, r):
            if s[i-1] != s[i]:
                ans += 1
        print(ans)
    elif com == 2:
        for i in range(l-1, r):
            s[i] = (s[i] + 1) % 26
