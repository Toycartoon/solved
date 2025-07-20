for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s = {*a}
    ans = 0
    while s:
        if a[ans] in s:
            s.remove(a[ans])
        ans += 1

    print(f"Case {t+1}: {ans}")
