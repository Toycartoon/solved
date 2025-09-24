from collections import deque

n, i = map(int, input().split())
a = deque([*range(1, n)])
a.rotate(i-1)
a.append(n)
for i in range(n // 2):
    print(f"{a[i]}-{a[-i-1]}")
