def f(s):
    for idx in range(len(s)-1, -1, -1):
        if s[idx] in "aeiou":
            return s[idx:]
    return s

for _ in range(int(input())):
    a = f(input().lower().split()[-1])
    b = f(input().lower().split()[-1])
    c = f(input().lower().split()[-1])
    d = f(input().lower().split()[-1])

    if a == b == c == d:
        print("perfect")
    elif a == b and c == d:
        print("even")
    elif a == c and b == d:
        print("cross")
    elif a == d and b == c:
        print("shell")
    else:
        print("free")
