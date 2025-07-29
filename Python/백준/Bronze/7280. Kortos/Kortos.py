d = set()
for i in "SBVK":
    for x in range(1, 14):
        d.add(f"{i} {x}")

for i in range(51):
    d.remove(input())

print(d.pop())
