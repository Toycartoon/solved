a = []
for i in range(4):
    a.append(int(input()))

if a.count(max(a)) < 3:
    print(0)
elif a.count(max(a)) == 4:
    print(1)
else:
    print(1 if min(a)+int(input()) == max(a) else 0)
