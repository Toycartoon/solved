for t in range(int(input())):
    _ = input()
    n = int(input())
    a = list(map(int, input().split()))

    s = set()
    for i in a:
        if i not in s:
            print(i, end=" ")
        s.add(i)
    print()
