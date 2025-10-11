for t in range(int(input())):
    n = int(input())
    s = input()

    upper, lower, digit, special = False, False, False, False
    for i in s:
        if i.isdigit():
            digit = True
        elif i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i in "#@*&":
            special = True

    if not upper:
        s += "A"
    if not lower:
        s += "a"
    if not digit:
        s += "1"
    if not special:
        s += "*"

    if len(s) < 7:
        s += "*" * (7-len(s))
    print(f"Case #{t+1}: {s}")
