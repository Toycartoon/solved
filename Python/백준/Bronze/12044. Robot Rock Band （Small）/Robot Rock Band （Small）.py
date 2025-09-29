for t in range(int(input())):
    n, k = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(4)]

    ans = 0
    for a in x[0]:
        for b in x[1]:
            for c in x[2]:
                for d in x[3]:
                    if a ^ b ^ c ^ d == k:
                        ans += 1
    print(f"Case #{t+1}: {ans}")
