a = int(input())
m, n = map(int, input().split())

print(min(max(m, n) / a * 2, max(max(m, n) / a, min(m, n)), min(m, n) / a * 2, max(max(m, n), min(m, n) / a)))
