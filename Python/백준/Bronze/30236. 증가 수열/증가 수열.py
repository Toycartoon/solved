for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 1
    for i in a:
        if i == ans:
            ans += 1
        ans += 1
    print(ans-1)
