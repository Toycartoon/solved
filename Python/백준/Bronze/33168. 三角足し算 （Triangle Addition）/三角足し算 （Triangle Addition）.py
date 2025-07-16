n = int(input())
a = list(map(int, input().split()))

while len(a) > 1:
    na = []
    for i in range(len(a)-1):
        na.append(a[i] + a[i+1])

    print(*na)
    a = na
