n, m = map(int, input().split())
a = list(map(int, input().split()))
print(sum(a) + min(n-m, m-1) + n-1)
