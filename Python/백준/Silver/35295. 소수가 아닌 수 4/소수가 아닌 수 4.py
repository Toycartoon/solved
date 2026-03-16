v = [True for _ in range(1001)]
v[0] = False
for i in range(2, len(v)):
    if not v[i]:
        continue
    for j in range(i*2, len(v), i):
        v[j] = False

n = int(input())
a = list(map(int, input().split()))

l = []
for i in a:
    if i != 1:
        l.append(i)
    if len(l) == 2:
        break

if len(l) == 2:
    print("YES")
    print(len(l))
    print(*l)
elif len(l) == 1 and not v[l[0]]:
    l.append(1)
    print("YES")
    print(len(l))
    print(*l)
else:
    print("NO")
