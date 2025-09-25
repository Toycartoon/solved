for i in range(int(input())):
    n, b = map(int, input().split())
    a = ""

    while n >= b:
        m = n % b
        n //= b
        if m < 10:
            a += str(m)
        else:
            a += chr(m + 55)
    m = n % b
    if m < 10:
        a += str(m)
    else:
        a += chr(m + 55)
    
    print(int(a[::-1] == a))
