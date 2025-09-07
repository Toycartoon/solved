d, m, w = map(int, input().split())
i, j, k = map(int, input().split())

a = (k-1) * (d * m) + (j-1) * d + i
print(chr(96 + a % w) if a % w != 0 else chr(96 + w))
