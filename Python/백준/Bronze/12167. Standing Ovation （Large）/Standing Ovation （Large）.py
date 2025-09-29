for t in range(int(input())):
    n, s = input().split()
    ans = 0
    c = int(s[0])
    for i in range(1, int(n)+1):
        if c >= i:
            c += int(s[i])
        else:
            ans += i-c
            c += int(s[i]) + 1

    print(f"Case #{t+1}: {ans}")
