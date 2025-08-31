g = [0 for _ in range(32)]
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    for v in range(a, b):
        g[v] += 1

k = int(input())
print(int(max(g) <= k))
