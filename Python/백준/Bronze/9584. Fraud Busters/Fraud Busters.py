import re

p = re.compile(input().replace("*", "."))

a = []
for i in range(int(input())):
    s = input()
    if re.match(p, s):
        a.append(s)

print(len(a))
for i in a:
    print(i)
