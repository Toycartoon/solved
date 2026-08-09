import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(2, n+1):
        v = n
        while v:
            if v % i != 0:
                break
            ans += 1
            v //= i
    print(ans)
