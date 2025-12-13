s = set()
for i in range(int(input())):
    v = input()
    v = v.replace("-", "").lower()
    s.add(v)
print(len(s))
