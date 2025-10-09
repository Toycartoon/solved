n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x.sort()
y.sort()
f = True
for i in range(n):
    if x[i] > y[i]:
        f = False
        break

if f:
    print("DA")
else:
    print("NE")
