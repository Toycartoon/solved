import sys

input = sys.stdin.readline

for t in range(int(input())):
    s = input().strip()
    l, r = map(int, input().split())

    ans = 0
    for i in range(l-1, r):
        if s[i % len(s)] == "B":
            ans += 1
    print(f"Case #{t+1}: {ans}")
