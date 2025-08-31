import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sorted(a, reverse=True)
mx = max(a)
sx = c[1]
for i in range(n):
    if a[i] == mx:
        print(a[i] - sx, end=" ")
    else:
        print(a[i] - mx, end=" ")
