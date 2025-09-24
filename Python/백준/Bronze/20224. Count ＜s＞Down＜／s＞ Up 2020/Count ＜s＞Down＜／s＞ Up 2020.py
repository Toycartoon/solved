while True:
    n = int(input())
    if n == 0:
        break

    a = list(map(int, input().split()))
    ans = 0
    for i in range(4, len(a)+1):
        if a[i-4:i] == [2,0,2,0]:
            ans += 1
    print(ans)
