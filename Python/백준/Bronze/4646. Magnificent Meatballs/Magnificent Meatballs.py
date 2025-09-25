while True:
    n, *a = map(int, input().split())
    if n == 0:
        break

    f = False
    for i in range(n):
        if sum(a[:i]) == sum(a[i:]):
            print(f"Sam stops at position {i} and Ella stops at position {i+1}.")
            f = True
            break

    if not f:
        print("No equal partitioning.")
