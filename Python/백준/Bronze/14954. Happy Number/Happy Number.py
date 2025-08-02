n = int(input())
s = set()

f = True
while True:
    if n in s:
        f = False
        break

    s.add(n)
    v = 0
    for i in str(n):
        v += int(i) ** 2
    n = v
    if n == 1:
        break

print("HAPPY" if f else "UNHAPPY")
