n, a, b = map(int, input().split())
l = []
for i in range(n-1):
    l.append(int(input()))

if a not in l and b not in l:
    print(-1)
elif a in l and b in l:
    for i in range(a, b+1):
        print(i)
elif a not in l:
    print(a)
elif b not in l:
    print(b)
else:
    print(-1)
