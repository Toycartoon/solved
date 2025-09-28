s = input().split(".")
for i in s:
    if i == "": continue
    print(*i.split()[::-1], end=". ")
