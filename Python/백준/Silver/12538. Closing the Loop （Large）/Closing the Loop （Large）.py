for t in range(int(input())):
    n = int(input())
    a = list(input().split())

    b, r = [], []
    for i in a:
        if i.endswith("B"):
            b.append(int(i[:-1]))
        elif i.endswith("R"):
            r.append(int(i[:-1]))

    b.sort(reverse=True)
    r.sort(reverse=True)

    ans = 0
    for i in range(min(len(b), len(r))):
        ans += b[i] + r[i] - 2
    print(f"Case #{t+1}: {ans}")
