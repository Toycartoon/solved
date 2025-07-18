import sys

input = sys.stdin.readline

while True:
    s = input().strip()

    if s == "#":
        break

    idx = -1
    for i in range(len(s)):
        if s[i] in "aeiou":
            idx = i
            break

    if idx == -1:
        print(s + "ay")
    else:
        print(s[idx:] + s[:idx] + "ay")
