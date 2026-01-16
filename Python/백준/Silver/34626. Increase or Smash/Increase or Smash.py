for t in range(int(input())):
    n = int(input())
    a = len(set(map(int, input().split())))
    print(a * 2 - 1)
