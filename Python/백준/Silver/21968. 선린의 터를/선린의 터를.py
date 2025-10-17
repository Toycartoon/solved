for t in range(int(input())):
    n = bin(int(input()))[2:]
    ans = 0
    for i in range(len(n)):
        if int(n[i]) == 1:
            ans += 3 ** (len(n)-i-1)
    print(ans)
