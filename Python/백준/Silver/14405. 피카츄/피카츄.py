import re

p = re.compile("(pi|ka|chu)+")
s = input()
if re.fullmatch(p, s):
    print("YES")
else:
    print("NO")
