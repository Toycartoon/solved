a, b, c = input().split()
if b == c:
    if a == b:
        print(a + b + c)
    else:
        print(a + b + b + a)
elif a == c:
    print(a + b + c)
else:
    print(a + b + c + b + a)
