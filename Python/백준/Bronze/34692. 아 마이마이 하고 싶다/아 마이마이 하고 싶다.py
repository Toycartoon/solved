n, m, k = map(int, input().split())
t = list(map(int, input().split()))

a = [0 for _ in range(m)]
for i in t:
    a[a.index(min(a))] += i

if min(a) > k:
    print("GO")
else:
    print("WAIT")
