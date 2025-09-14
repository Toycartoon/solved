s = input()
w = [0 for _ in range(26)]

for i in s:
    w[ord(i)-97] += 1

o = 0
for i in w:
    if i != 0:
        if i % 2 == 1:
            o += 1

print(max(0, o-1))
