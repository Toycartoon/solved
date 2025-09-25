n = int(input())
h = list(map(int, input().split()))
t = int(input())

a = []
for i in h:
    a.append((t % i, i))
a.sort()
print(a[0][1])
