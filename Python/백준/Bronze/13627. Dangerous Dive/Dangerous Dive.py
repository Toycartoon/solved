n, r = map(int, input().split())
a = list(range(1, n+1))

for i in list(map(int, input().split())):
    a.remove(i)

if len(a) > 0:
    print(*a)
else:
    print("*")
