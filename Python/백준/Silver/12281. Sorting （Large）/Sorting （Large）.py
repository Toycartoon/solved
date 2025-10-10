for t in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    a = []
    b = []
    for i in s:
        if i % 2 == 0:
            b.append(i)
        else:
            a.append(i)

    a.sort()
    b.sort(reverse=True)
    idx_a, idx_b = 0, 0
    print(f"Case #{t+1}: ", end="")
    for i in s:
        if i % 2 == 0:
            print(b[idx_b], end=" ")
            idx_b += 1
        else:
            print(a[idx_a], end=" ")
            idx_a += 1
    print()
