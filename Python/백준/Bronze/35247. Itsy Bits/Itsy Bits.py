from math import ceil, log2

n = int(input())
b = ceil(log2(n + 1))

ans = 1
while ans < b:
    ans <<= 1

print(ans, "bit" if ans == 1 else "bits")
