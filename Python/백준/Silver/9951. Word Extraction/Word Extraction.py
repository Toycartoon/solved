import re

while True:
    s = input()
    if s == "#":
        break

    s = re.sub("[^ \\w]", "", s)
    v = set()
    for i in s.split():
        if len(i) == 0 or i.isdigit() or i.lower() in v:
            continue
        v.add(i.lower())

    for i in sorted(list(v)):
        print(i)
    print()
