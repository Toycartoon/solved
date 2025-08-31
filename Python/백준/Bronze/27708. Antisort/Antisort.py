t = int(input())
print(t)
for i in range(t):
    print(input())
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    print(n)
    print(a[1], a[0], *a[2:])
