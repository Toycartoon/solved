for t in range(int(input())):
    n, k, s = map(int, input().split())
    print(f"Case #{t+1}: {min(n+k, 2*k+n-2*s)}")
