n = int(input())
red = 0

a = {"yellow": 2, "green": 3, "brown": 4, "blue": 5, "pink": 6, "black": 7}
l = []
for i in range(n):
    s = input()
    if s == "red":
        red += 1
    else:
        l.append(a[s])
l.sort()
ans = 0
if len(l) == 0:
    print(1)
else:
    print(sum(l) + red + red * l[-1])
