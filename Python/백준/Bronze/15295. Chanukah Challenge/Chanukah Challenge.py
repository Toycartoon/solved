for _ in range(int(input())):
    k, p = map(int, input().split())

    ans = p
    for i in range(1, p+1):
        ans += i

    print(k, ans)
