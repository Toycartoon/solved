n, m = map(int, input().split())
print((pow(2, n+1, m) + (pow(2, n-1, m)-1 if n > 0 else 0)) % m)
