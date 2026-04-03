n = int(input())
s = input()

r = []
for i in s:
    r.append(i)
    if len(r) >= 2 and r[-2] == r[-1]:
        for _ in range(2):
            r.pop()
    elif len(r) >= 3 and r[-3] == r[-1]:
        for _ in range(3):
            r.pop()

if len(r) == 0:
    print(-1)
else:
    print(*r, sep="")
