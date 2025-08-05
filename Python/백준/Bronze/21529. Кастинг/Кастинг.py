t = int(input())
n, *a = map(int, input().split())

a.sort()
if t == 1:
    print(max(a[0]-(n-a[1])-(n-a[2]), 0))
elif t == 2:
    print(a[0])
