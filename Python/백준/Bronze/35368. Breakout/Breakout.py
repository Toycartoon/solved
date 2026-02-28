n, x, m = map(int, input().split())
a = [0 for _ in range(n)]
for i in range(m):
    a[int(input())-1] += 1
print(min(sum(a[:x-1]), sum(a[x-1:])))
