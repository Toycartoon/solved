import re

p = re.compile("\\d+")
s = input()
print(len(set(re.findall(p, s))))
