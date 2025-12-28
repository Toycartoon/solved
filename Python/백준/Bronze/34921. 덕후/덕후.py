age, tier = map(int, input().split())
p = 10 + 2 * (25 - age + tier)
print(max(p, 0))
