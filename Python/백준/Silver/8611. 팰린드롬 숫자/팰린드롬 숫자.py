d = int(input())

p = False
for b in range(2, 11):
    n = d
    a = ""

    while n >= b:
        m = n % b
        n //= b
        a += str(m)
    m = n % b
    a += str(m)

    if a == a[::-1]:
        print(b, a[::-1])
        p = True

if not p:
    print("NIE")
