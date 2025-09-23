import sys

input = sys.stdin.readline

for t in range(int(input())):
    mn = float('inf')
    ans = ""
    s = input().strip()
    for i in range(int(input())):
        w = input().strip()
        cnt = 0
        for x in range(len(s)):
            if s[x] != w[x]:
                cnt += 1

        if mn > cnt:
            mn = cnt
            ans = w
    print(ans)
