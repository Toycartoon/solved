import re

p = re.compile("([+]|[-])?[0-9]+([.][0-9]+)?([eE]([+]|[-])?[0-9]+)?")
for t in range(int(input())):
    s = input().strip()
    if re.fullmatch(p, s):
        print("LEGAL")
    else:
        print("ILLEGAL")
