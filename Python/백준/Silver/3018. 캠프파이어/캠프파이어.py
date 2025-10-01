n = int(input())
a = [set() for _ in range(n+1)]
s = 0
for e in range(int(input())):
    m, *k = map(int, input().split())
    if 1 in k:
        for i in k:
            a[i].add(s)
        s += 1
    else:
        for i in k:
            for j in k:
                a[i].update(a[j])

for i in range(1, n+1):
    if len(a[i]) == s:
        print(i)
