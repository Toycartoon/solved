import sys

input = sys.stdin.readline

a1 = []
a2 = []
a = 0
b = 0
for i in range(int(input())):
    n = int(input())
    a += n ** 2
    b += n
    a1.append(a)
    a2.append(b)

ans = 0
for i in range(len(a1)):
    ans = max(ans, a1[i] * (a2[-1] - a2[i]))

print(ans)
