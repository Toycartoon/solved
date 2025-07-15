a = [0 for _ in range(11)]
b = [0 for _ in range(11)]

av, bv = 0, 0
for i in map(int, input().split()):
    a[i] += 1
    av += i

for i in map(int, input().split()):
    b[i] += 1
    bv += i

if av > bv:
    print("Algosia")
elif bv > av:
    print("Bajtek")
else:
    f = True
    for i in range(10, -1, -1):
        if a[i] > b[i]:
            print("Algosia")
            f = False
            break
        elif a[i] < b[i]:
            print("Bajtek")
            f = False
            break

    if f:
        print("remis")
