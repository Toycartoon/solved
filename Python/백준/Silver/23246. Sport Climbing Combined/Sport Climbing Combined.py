a = []
for i in range(int(input())):
    b, p, q, r = map(int, input().split())
    a.append((p * q * r, p + q + r, b))

a.sort()
for i in range(3):
    print(a[i][2], end=" ")
