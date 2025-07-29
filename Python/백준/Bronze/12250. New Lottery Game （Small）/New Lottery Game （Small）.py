for t in range(int(input())):
    a, b, k = map(int, input().split())
    ans = 0
    for i in range(a):
        for j in range(b):
            if i & j < k:
                ans += 1

    print(f"Case #{t+1}: {ans}")
