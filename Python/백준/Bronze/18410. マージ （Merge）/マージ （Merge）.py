n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
while a and b:
    if a[0] <= b[0]:
        c.append(a[0])
        a.pop(0)
    else:
        c.append(b[0])
        b.pop(0)

c += a + b
for i in c:
    print(i)
