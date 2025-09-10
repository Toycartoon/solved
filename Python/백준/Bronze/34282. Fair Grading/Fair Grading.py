x, y, z = map(int, input().split())
s = x * 0.25 + y * 0.25 + z * 0.5

if s >= 90:
    print("A")
elif s >= 80:
    print("B")
elif s >= 70:
    print("C")
elif s >= 60:
    print("D")
else:
    print("F")
