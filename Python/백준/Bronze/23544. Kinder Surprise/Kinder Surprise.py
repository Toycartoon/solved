n = int(input())
s = set()

for i in range(n):
    s.add(input())

print(n-len(s))
