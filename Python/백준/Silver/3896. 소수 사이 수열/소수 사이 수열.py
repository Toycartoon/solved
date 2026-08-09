import sys

input = sys.stdin.readline

a = [i for i in range(1299710)]
for i in range(2, int(len(a) ** 0.5) + 1):
    if a[i] == 0:
        continue
    for j in range(i * i, len(a), i):
        a[j] = 0

s = []
for i in a:
    if i != 0:
        s.append(i)

for t in range(int(input())):
    k = int(input())

    if a[k] != 0:
        print(0)
        continue

    for i in range(1, len(s)):
        if k < s[i]:
            print(s[i] - s[i-1])
            break
