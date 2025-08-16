import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    s = {*input().strip()}

    ans = 0
    for i in range(n):
        v = {*input().strip()}
        if len(s & v) > 0:
            ans += 1

    print(f"Data Set {t+1}:")
    print(ans, end="\n\n")
