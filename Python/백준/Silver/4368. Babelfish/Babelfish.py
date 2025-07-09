import sys

input = sys.stdin.readline

a = {}
while True:
    s = input().strip()

    if s == "":
        break

    s = s.split()
    a[s[1]] = s[0]


while True:
    s = input().strip()

    if s == "":
        break

    if s in a:
        print(a[s])
    else:
        print("eh")
