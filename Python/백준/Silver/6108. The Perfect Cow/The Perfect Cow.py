n = int(input())
a = []
for i in range(n):
    v = list(map(int, input().split()))
    v.sort()
    a.append(v[n//2])
a.sort()
print(a[n//2])
