w = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]
while True:
    try:
        s = input()
        ans = ""
        for i in range(len(s)-1):
            if w[ord(s[i])-65] != w[ord(s[i+1])-65] and w[ord(s[i])-65] != 0:
                ans += str(w[ord(s[i])-65])

        if w[ord(s[-1])-65] != 0:
            ans += str(w[ord(s[-1])-65])

        print(ans)
    except EOFError:
        break
