j, r = map(int, input().split())
p = list(map(int, input().split()))

a = [0 for _ in range(j)]
for i in range(j * r):
    a[i % j] += p[i]
print(j-a[::-1].index(max(a)))
