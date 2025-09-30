f = [1]
n = int(input())
if n == 0:
    print("NO")
    exit()

a = 1
x = 1
while a <= n:
    a *= x
    f.append(a)
    x += 1

for i in range(len(f)-1, -1, -1):
    if f[i] <= n:
        n -= f[i]

if n == 0:
    print("YES")
else:
    print("NO")
