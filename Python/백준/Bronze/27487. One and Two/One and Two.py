for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = a.count(2)
    if k % 2 == 1:
        print(-1)
        continue

    for i in range(1, n):
        if a[:i].count(2) == a[i:].count(2):
            print(i)
            break
