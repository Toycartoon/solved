for t in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    v = 0
    for i in range(n // 2):
        if s[i] != s[n-i-1]:
            v += 1
    print(f"Case #{t+1}: {abs(k-v)}")
