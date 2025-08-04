import sys

input = sys.stdin.readline

while True:
    s = input().strip()
    if s == "#":
        break

    f = False
    for i in range(len(s)):
        x = s[:i] + s[i+1:]
        if x == x[::-1]:
            print(x)
            f = True
            break

    if not f:
        print("not possible")
