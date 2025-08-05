a = list(map(int, input().split()))
n = a.index(int(input()))

if n < 5:
    print("A+")
elif n < 15:
    print("A0")
elif n < 30:
    print("B+")
elif n < 35:
    print("B0")
elif n < 45:
    print("C+")
elif n < 48:
    print("C0")
else:
    print("F")
