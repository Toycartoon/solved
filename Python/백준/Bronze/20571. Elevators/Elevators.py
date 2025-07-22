s, n = input().split()
n = int(n)

if s == "residential":
    if n <= 1:
        print(0)
    elif n <= 5:
        print(1)
    elif n <= 10:
        print(2)
    elif n <= 15:
        print(3)
    elif n <= 20:
        print(4)
elif s == "commercial":
    if n <= 1:
        print(0)
    elif n <= 7:
        print(1)
    elif n <= 14:
        print(2)
    elif n <= 20:
        print(3)
elif s == "industrial":
    if n <= 1:
        print(0)
    elif n <= 4:
        print(1)
    elif n <= 8:
        print(2)
    elif n <= 12:
        print(3)
    elif n <= 16:
        print(4)
    elif n <= 20:
        print(5)
