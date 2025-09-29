n = int(input())
a = list(map(int, input().split()))
print(max(n-a[::-1].index(1)-a.index(0)-1, n-a[::-1].index(0)-a.index(1)-1))