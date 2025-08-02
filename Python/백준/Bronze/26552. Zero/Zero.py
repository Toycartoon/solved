for t in range(int(input())):
    n = int(input())
    ans = n + 1
    while True:
        if "0" in str(ans):
            ans += 1
        else:
            break

    print(ans)
