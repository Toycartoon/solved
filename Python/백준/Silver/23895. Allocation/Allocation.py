for t in range(int(input())):
    n, b = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    ans = 0
    for i in a:
        if b-i < 0:
            break
        b -= i
        ans += 1
    print(f"Case #{t+1}: {ans}")
