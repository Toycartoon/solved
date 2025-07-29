a = list(map(int, input().split()))
b = list(map(int, input().split()))

if max(a) > max(b):
    a[a.index(max(a))] -= max(b)
    b[b.index(max(b))] = 0
else:
    b[b.index(max(b))] -= max(a)
    a[a.index(max(a))] = 0

print(sum(a) + sum(b))
