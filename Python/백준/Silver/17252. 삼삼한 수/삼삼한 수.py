n = int(input())
if n == 1:
    print("YES")
    exit()

a = [1]
x = 1
v = 0

f = True
while a[-1] < n and f:
    v = 3 ** x
    a.append(v)
    if v == n:
        f = False
        break
    for i in range(len(a)-1):
        if v + a[i] == n:
            f = False
            break
        a.append(v + a[i])
    x += 1

if f:
    print("NO")
else:
    print("YES")
