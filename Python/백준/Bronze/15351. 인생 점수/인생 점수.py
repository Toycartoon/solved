for i in range(int(input())):
    s = input()
    ans = 0
    for v in s:
        if v.isalpha():
            ans += ord(v) - 64

    if ans == 100:
        print("PERFECT LIFE")
    else:
        print(ans)
