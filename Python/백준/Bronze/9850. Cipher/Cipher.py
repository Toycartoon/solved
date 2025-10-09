s = input()
for i in range(1, 26):
    a = ""
    for v in s:
        if v.isalpha():
            a += chr(ord(v) + i if ord(v) + i <= 90 else ord(v) + i - 26)
        else:
            a += v

    if "CHIPMUNKS" in a and "LIVE" in a:
        print(a)
