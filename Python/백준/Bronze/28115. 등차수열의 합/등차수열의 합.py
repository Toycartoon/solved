n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print("YES")
    print(a[0])
    print(0)
    exit()

d = a[1]-a[0]
f = True
for i in range(1, n):
    if a[i]-a[i-1] != d:
        f = False
        break

if not f:
    print("NO")
else:
    print("YES")
    print(*a)
    print(*[0] * n)
