a = []
s = 0
for i in range(1, 142):
    for j in range(i):
        s += i
        a.append(s)

while True:
    n = int(input())
    if n == 0:
        break
    print(n, a[n-1])
