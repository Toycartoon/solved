for t in range(int(input())):
    s = input().replace("-", "").lower()
    v = ""
    for i in s:
        v += chr(122-(ord(i)-97))

    if sorted([*v]) == sorted([*s]):
        print("Yes")
    else:
        print("No")
