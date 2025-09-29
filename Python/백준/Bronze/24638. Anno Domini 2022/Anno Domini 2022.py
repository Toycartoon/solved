a, b = input().split()
c, d = input().split()

if a == "AD":
    n = int(b)
elif b == "BC":
    n = -int(a)

if c == "AD":
    m = int(d)
elif d == "BC":
    m = -int(c)

if n * m < 0:
    print(abs(n-m)-1)
else:
    print(abs(n-m))
