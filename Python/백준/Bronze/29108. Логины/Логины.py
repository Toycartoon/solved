import re

p = re.compile("io[0-9]+")
s = input()

if re.match(p, s):
    print("Correct")
else:
    print("Incorrect")
