n, m = map(int, input().split())
k, *d = map(int, input().split())

a = []
for i in range(n):
    v, *p = map(int, input().split())
    a.append(p)

s = set()
for i in d:
    s.update({*a[i-1]})
print("yes" if s == {*range(1, m+1)} else "no")
