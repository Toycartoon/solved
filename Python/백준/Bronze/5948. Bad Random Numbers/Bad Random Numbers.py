n = int(input())
s = set()
while n not in s:
    s.add(n)
    n = ((n // 100) % 10 * 10 + (n // 10) % 10) ** 2
print(len(s))
