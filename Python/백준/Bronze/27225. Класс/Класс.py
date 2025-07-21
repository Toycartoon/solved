n = int(input())
m = int(input())
print(min(n, m) * 2 + (max(n, m) - min(n, m)) % 2)
