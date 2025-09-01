a = input()
s = 0
for i in range(len(a)):
    if i % 2 == 0:
        s += sum(map(int, [*str(int(a[i]) * 2)]))
    else:
        s += int(a[i])

if s % 10 == 0:
    print("DA")
else:
    print("NE")
