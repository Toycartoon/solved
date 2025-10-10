from itertools import permutations as perm

a = []
for i in perm("0123456789", 10):
    if i[0] == "0":
        continue

    if int("".join(i[:5])) % int("".join(i[5:])) == 0 and int("".join(i[:5])) // int("".join(i[5:])) == 9:
        a.append(("".join(i[:5]), "".join(i[5:])))
print(*a[int(input())-1])
