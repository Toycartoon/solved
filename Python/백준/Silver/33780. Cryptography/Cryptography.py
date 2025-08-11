n = int(input())

f = True if n > 1 else False
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        f = False
        break

if f:
    print("SAFE")
else:
    print("BROKEN")
