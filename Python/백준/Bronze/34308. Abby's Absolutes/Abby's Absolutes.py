n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in a:
    if abs(i-n) < abs(1-i):
        print(n, end=" ")
    else:
        print(1, end=" ")
