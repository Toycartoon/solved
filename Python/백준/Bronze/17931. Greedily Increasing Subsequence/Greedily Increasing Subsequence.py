n = int(input())
a = list(map(int, input().split()))

g = [a[0]]
for i in range(1, n):
    if a[i] > g[-1]:
        g.append(a[i])

print(len(g))
print(*g)
