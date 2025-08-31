for t in range(int(input())):
    n = int(input())
    a = list(input().split())
    b = list(input().split())

    if sorted(a) == sorted(b):
        print("NOT CHEATER")
    else:
        print("CHEATER")
