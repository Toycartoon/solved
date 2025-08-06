n, k = input().split()
m = int(n)
n = int(k + n)

f = True
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        f = False
        break
        
for i in range(2, int(m ** 0.5) + 1):
    if m % i == 0:
        f = False
        break

if f:
    print("Yes")
else:
    print("No")
