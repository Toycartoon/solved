from fractions import Fraction as f

n = int(input())
s = set()
for i in range(1, n+1):
    for j in range(i+1):
        s.add(f(j, i))

a = list(s)
a.sort()
print(len(a))
for i in a:
    if i == 0 or i == 1:
        print(f"{i}/1")
    else:
        print(i)
