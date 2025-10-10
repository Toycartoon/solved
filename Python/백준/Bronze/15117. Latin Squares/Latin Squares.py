n = int(input())
a = [[*input()] for _ in range(n)]

f = True
for i in range(n):
    if len({*a[i]}) != n:
        f = False
        break

for i in range(n):
    if len({*list(zip(*a))[i]}) != n:
        f = False
        break

if f:
    if sorted(a[0]) == a[0] and sorted(list(zip(*a))[0]) == list(list(zip(*a))[0]):
        print("Reduced")
    else:
        print("Not Reduced")
else:
    print("No")
