for t in range(int(input())):
    a = []
    for i in range(int(input())):
        a.append(input())

    s = set()
    for i in range(int(input())):
        s.update(input().split())

    print(f"Test set {t+1}:")
    for i in a:
        if i in s:
            print(f"{i} is present")
        else:
            print(f"{i} is absent")
    print()
