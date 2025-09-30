for t in range(int(input())):
    s = input()
    f = 0
    for i in range(6, len(s)+1):
        if f != 0:
            break

        for j in range(i, len(s)+1):
            upper, lower, digit = False, False, False
            for k in s[j-i:j]:
                if k.isupper():
                    upper = True
                elif k.islower():
                    lower = True
                elif k.isdigit():
                    digit = True

            if upper and lower and digit and f == 0:
                f = i
                break
    print(f)
