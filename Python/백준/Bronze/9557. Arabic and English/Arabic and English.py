for t in range(int(input())):
    n = int(input())
    a = input().split()

    f = True
    for idx in range(n):
        if a[idx].isalpha():
            print(*(a[idx+1:] + [a[idx]] + a[:idx]))
            f = False
            break
    if f:
        print(*a)
