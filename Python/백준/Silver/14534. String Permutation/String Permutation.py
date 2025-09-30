from itertools import permutations as perm

for t in range(int(input())):
    s = input()
    print(f"Case # {t+1}:")
    for v in perm([*s], len(s)):
        print(*v, sep="")
