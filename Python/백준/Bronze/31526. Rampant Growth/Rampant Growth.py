r, c = map(int, input().split())
print(r * ((r-1) ** (c-1)) % 998244353)
