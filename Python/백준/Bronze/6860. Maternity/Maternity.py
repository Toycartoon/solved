a = input()
b = input()
for t in range(int(input())):
    s = input()
    f = True
    for i in range(5):
        if s[i].isupper():
            if a[i * 2].islower() and b[i * 2].islower():
                f = False
                break
        elif s[i].islower():
            if a[i * 2 + 1].isupper() or b[i * 2 + 1].isupper():
                f = False
                break

    if f:
        print("Possible baby.")
    else:
        print("Not their baby!")
