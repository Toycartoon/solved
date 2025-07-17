a = list(map(int, input().split()))
b = list(map(int, input().split()))

n, m = 0, 0
for i in range(10):
    if a[i] > b[i]:
        n += 1
    elif a[i] < b[i]:
        m += 1

if n > m:
    print("A")
elif n < m:
    print("B")
else:
    print("D")
