goshuzin = input()
s = set(goshuzin)

for i in range(int(input())):
    z1, z2 = input().split()
    if z2 == goshuzin:
        s.add(z1)
        goshuzin = z1

print(goshuzin)
print(len(s))
