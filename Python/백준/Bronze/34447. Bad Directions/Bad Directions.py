for t in range(int(input())):
    k, n = map(int, input().split())
    for i in str(n):
        print((int(i) + k) % 10, end='')
    print()
