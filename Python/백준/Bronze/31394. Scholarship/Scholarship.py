n = int(input())

named = True
mix = True
s = 0
for i in range(n):
    m = int(input())
    s += m
    if m != 5:
        named = False
    if m == 3:
        mix = False

if not mix:
    print("None")
elif named:
    print("Named")
elif s / n >= 4.5:
    print("High")
else:
    print("Common")
