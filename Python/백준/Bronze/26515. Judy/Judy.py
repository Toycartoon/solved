for t in range(int(input())):
    a = list(map(int, input().split()))
    ans = []
    for i in a:
        if 65 <= i <= 90 or 97 <= i <= 122:
            ans.append(chr(i).lower())
        else:
            ans.append("-")
    print(*ans[1:], ans[0], "ay", sep="")
