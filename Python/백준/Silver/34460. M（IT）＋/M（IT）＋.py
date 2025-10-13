import re

p = re.compile("(M(IT)+)+")
for t in range(int(input())):
    n = int(input())
    s = input()
    if re.fullmatch(p, s):
        print("YES")
    else:
        print("NO")
