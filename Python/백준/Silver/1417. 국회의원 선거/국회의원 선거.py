a = []
for i in range(int(input())):
    a.append(int(input()))

v = a[0]
a = a[1:]
ans = 0
while len(a) >= 1 and a[a.index(max(a))] >= v:
    v += 1
    a[a.index(max(a))] -= 1
    ans += 1

print(ans)
