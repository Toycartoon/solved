from math import ceil

small, medium, large = 0, 0, 0
for n in range(int(input())):
    s, l = input().split()
    if s == "S":
        small += int(l)
    elif s == "M":
        medium += int(l)
    elif s == 'L':
        large += int(l)

print(ceil(small / 6) + ceil(medium / 8) + ceil(large / 12))
