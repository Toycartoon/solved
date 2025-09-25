k, p, x = map(int, input().split())
mn = float('inf')
m = 1
while True:
    v = x * m + p * (k / m)
    if mn <= v:
        break
    else:
        mn = v
    m += 1
print(f"{mn:.3f}")
