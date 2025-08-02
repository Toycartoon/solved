x, k, a = map(int, input().split())
print(int(x - (k + a) * (x // (k + a)) < k))
