for t in range(int(input())):
    x = int(input())
    l = list(map(int, input().split()))
    a = []
    for i in range(1, 2 * x + 1, 2):
        a.append(l[i] / l[i-1])
    print(a.index(min(a))+1)