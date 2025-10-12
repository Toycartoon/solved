n = int(input())
x = list(map(int, input().split()))

a, b = 0, 0
x.sort(reverse=True)
for i in range(n):
    if i % 2 == 0:
        a += x[i]
    else:
        b += x[i]
print(a, b)
