import sys

input = sys.stdin.readline

ms, js = 0, 0
mp, jp = 0, 0
for i in range(int(input())):
    x, p = input().split()

    if x == "M":
        mp += 1
        ms += int(p)
    elif x == "J":
        jp += 1
        js += int(p)


m = (ms / mp) if mp != 0 else 0
j = (js / jp) if jp != 0 else 0

if m > j:
    print("M")
elif j > m:
    print("J")
else:
    print("V")
