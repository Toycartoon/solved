import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

v = []
for i in range(n):
    for j in range(i+1, n):
        if a[i] == a[j]:
            if j-i <= k:
                v.append(a[i])
            break
print(max(v))
