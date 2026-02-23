while True:
    n = int(input())
    if n == 0:
        break

    s = input()
    x = 0
    for i in range(len(s)-1, 0, -1):
        if s[:i] == s[-i:]:
            x = i
            break
    print(s + s[x:])
