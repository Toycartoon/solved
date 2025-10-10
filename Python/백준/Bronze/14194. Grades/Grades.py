for t in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))

    a = (min(v) + max(v)) / 2
    b = sum(v) / n
    if abs(a-b) <= 1:
        print("Yes")
    else:
        print("No")
