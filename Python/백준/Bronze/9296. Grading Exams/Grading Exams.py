for t in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    ans = 0
    for i in range(n):
        if a[i] != b[i]:
            ans += 1

    print(f"Case {t+1}: {ans}")
