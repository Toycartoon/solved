w = set()
y, m = 2018, 4
while y <= 10000:
    w.add(y)
    m += 26
    y += m // 12
    m = m % 12
    if m == 0:
        y -= 1
        m = 12

if int(input()) in w:
    print("yes")
else:
    print("no")
