import re

for t in range(int(input())):
    n, *a = input().split()
    a.sort(key=lambda x: (-len(re.findall("[aeiou]+", x)), x))
    print(*a)
