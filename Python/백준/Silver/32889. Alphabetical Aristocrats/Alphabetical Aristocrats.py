import re

p = re.compile("[A-Z].+")

a = []
for i in range(int(input())):
    a.append(input())

for i in sorted(a, key=lambda x: re.findall(p, x)):
    print(i)
