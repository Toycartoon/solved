n, m = map(int, input().split())
a = list(input().split())
b = list(input().split())

for i in range(int(input())):
    t = int(input())
    print(a[t%n-1]+b[t%m-1])
