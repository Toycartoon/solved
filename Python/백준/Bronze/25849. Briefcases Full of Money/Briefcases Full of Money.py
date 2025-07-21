a, b, c, d, e, f = map(int, input().split())

b *= 5
c *= 10
d *= 20
e *= 50
f *= 100

mx = max(a, b, c, d, e, f)
if mx == f:
    print(100)
elif mx == e:
    print(50)
elif mx == d:
    print(20)
elif mx == c:
    print(10)
elif mx == b:
    print(5)
elif mx == a:
    print(1)
