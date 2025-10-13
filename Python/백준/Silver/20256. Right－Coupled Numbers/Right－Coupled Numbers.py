for t in range(int(input())):
    x = int(input())
    f = False
    for a in range(1, int(x ** 0.5)+1):
        if x % a != 0:
            continue
        b = x // a
        if a <= b and a / b >= 0.5:
            f = True
            break
    print(int(f))
