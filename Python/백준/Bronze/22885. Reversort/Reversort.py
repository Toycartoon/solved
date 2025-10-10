for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n-1):
        j = a.index(min(a[i:]))
        ans += j-i+1
        a[i:j+1] = a[i:j+1][::-1]
    print(f"Case #{t+1}: {ans}")
