l, h, p, e, n = map(int, input().split())
a, b, c, d = (0, 0), (0, 0), (0, 0), (0, 0)
for i in range(n):
    sub, _, per = input().split()
    r, s = map(int, per.split("/"))
    if sub == "Lab":
        a = (a[0]+r, a[1]+s)
    elif sub == "Hw":
        b = (b[0]+r, b[1]+s)
    elif sub == "Proj":
        c = (c[0]+r, c[1]+s)
    elif sub == "Exam":
        d = (d[0]+r, d[1]+s)
print(int(l * a[0] / a[1] + h * b[0] / b[1] + p * c[0] / c[1] + e * d[0] / d[1]))
