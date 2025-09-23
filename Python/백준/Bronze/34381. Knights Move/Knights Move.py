s = input()
a = []
for dx, dy in [(2, 1), (1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2), (-2, 1), (-1, 2)]:
    if 97 <= ord(s[0]) + dx <= 104 and 1 <= int(s[1]) + dy <= 8:
        a.append(chr(ord(s[0]) + dx) + str(int(s[1]) + dy))

a.sort()
for i in a:
    print(i)
