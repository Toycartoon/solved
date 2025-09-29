k = int(input())
s = []
x = 1
while len(s) <= k:
    s.extend([*str(x ** 3)])
    x += 1
print(s[k-1])
