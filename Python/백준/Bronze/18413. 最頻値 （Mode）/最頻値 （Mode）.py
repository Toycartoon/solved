n, m = map(int, input().split())
a = list(map(int, input().split()))

b = []
for i in range(1, m+1):
    b.append(a.count(i))

print(max(b))
