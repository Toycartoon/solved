import sys

input = sys.stdin.readline

a = []
for i in range(int(input())):
    s = input().strip()
    if s == "TRUTH":
        a.append(True)
    elif s == "LIE":
        a.append(False)

for i in range(len(a)-1, 0, -1):
    if not a[i]:
        a[i-1] = not a[i-1]

print("TRUTH" if a[0] else "LIE")
