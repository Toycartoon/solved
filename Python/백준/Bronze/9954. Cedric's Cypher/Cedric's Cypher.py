while True:
    s = input()
    if s == "#":
        break

    v = ord("A") - ord(s[-1])
    for i in s[:-1]:
        if i.isupper():
            print(chr(ord(i)+v if 65 <= ord(i)+v else ord(i)+v+26), end="")
        elif i.islower():
            print(chr(ord(i)+v if 97 <= ord(i)+v else ord(i)+v+26), end="")
        else:
            print(i, end="")
    print()
