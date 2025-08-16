for t in range(int(input())):
    v = []
    ans = 0
    for n in range(int(input())):
        a, b = map(int, input().split())
        for i in v:
            if (i[0] < a and i[1] > b) or (i[0] > a and i[1] < b):
                ans += 1
        v.append((a, b))

    print(f"Case #{t+1}: {ans}")
