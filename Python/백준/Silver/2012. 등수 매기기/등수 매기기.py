import sys

input = sys.stdin.readline

a = []
for i in range(int(input())):
    a.append(int(input()))

ans = 0
a.sort()
for i in range(len(a)):
    ans += abs(a[i] - (i+1))

print(ans)
