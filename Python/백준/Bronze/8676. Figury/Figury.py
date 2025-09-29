n = int(input())
a = list(map(int, input().split()))

f = False
for i in range(3, n+1):
    if len({*range(3)}-{*a[i-3:i]}) == 0:
        f = True
        break

if f:
    print("TAK")
else:
    print("NIE")