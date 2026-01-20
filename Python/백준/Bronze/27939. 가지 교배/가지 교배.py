n = int(input())
s = input().split()
m, k = map(int, input().split())
f = False
for i in range(m):
    a = list(map(int, input().split()))
    v = set()
    for x in a:
        v.add(s[x-1])

    if len(v) == 1 and v.pop() == "W":
        f = True
        break

if f:
    print("W")
else:
    print("P")
