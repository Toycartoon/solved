n, k = map(int, input().split())
s = input().split()

v = 0
a = []
for i in s:
    if v + len(i) <= k:
        a.append(i)
        v += len(i)
    else:
        print(*a)
        a.clear()
        a.append(i)
        v = len(i)
print(*a)
