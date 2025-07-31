a, b, c = map(int, input().split())
print(a ^ b if c % 2 == 1 else (a ^ b) ^ b)
