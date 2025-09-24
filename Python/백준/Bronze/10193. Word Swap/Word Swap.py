for t in range(int(input())):
    a, b = input().split()
    c = 0
    for i in range(len(a)):
        c += ord(a[i]) - ord(b[i])

    if c > 0:
        print(f"Swapping letters to make {a} look like {b} earned {c} coins.")
    elif c < 0:
        print(f"Swapping letters to make {a} look like {b} cost {abs(c)} coins.")
    else:
        print(f"Swapping letters to make {a} look like {b} was FREE.")
