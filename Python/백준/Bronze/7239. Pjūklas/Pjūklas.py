n = int(input())
a = list(map(int, input().split()))

a.sort()
u, v = a[:n//2], a[n//2:]
for i in range(n):
    if i % 2 == 0:
        print(v[i//2], end=" ")
    else:
        print(u[(i-1)//2], end=" ")
